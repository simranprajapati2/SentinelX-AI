from flask import (
    Blueprint,
    render_template,
    request
)

from flask_login import login_required

from utils.website_checker import (
    check_website
)

from models.blocked_domain import (
    BlockedDomain
)

website = Blueprint(
    "website",
    __name__,
    url_prefix="/website"
)


@website.route(
    "/",
    methods=["GET", "POST"]
)
@login_required
def verify():

    result = None

    if request.method == "POST":

        url = request.form.get(
            "website_url"
        )

        result = check_website(
            url
        )

        if result["valid"]:

            blocked = (
                BlockedDomain.query.filter_by(
                    domain=result["domain"]
                ).first()
            )

            if blocked:

                result["warnings"].append(
                    "Domain found in blacklist."
                )

                result["risk_score"] += 50

                if result["risk_score"] > 100:
                    result["risk_score"] = 100

    return render_template(
        "website/verify_website.html",
        result=result
    )