import os
from werkzeug.utils import secure_filename

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    current_app
)

from flask_login import (
    login_required,
    current_user
)

from extensions import db
from forms.profile_form import ProfileForm

profile = Blueprint(
    "profile",
    __name__,
    url_prefix="/profile"
)


@profile.route("/")
@login_required
def view_profile():

    return render_template(
        "profile/profile.html",
        user=current_user
    )


@profile.route(
    "/edit",
    methods=["GET", "POST"]
)
@login_required
def edit_profile():

    form = ProfileForm()

    if form.validate_on_submit():

        current_user.full_name = form.full_name.data
        current_user.phone = form.phone.data
        current_user.bio = form.bio.data

        image = request.files.get(
            "profile_image"
        )

        if image and image.filename != "":

            filename = secure_filename(
                image.filename
            )

            upload_folder = os.path.join(
                current_app.root_path,
                "static",
                "uploads",
                "profile"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            save_path = os.path.join(
                upload_folder,
                filename
            )

            image.save(save_path)

            current_user.profile_image = filename

        db.session.commit()

        flash(
            "Profile updated successfully.",
            "success"
        )

        return redirect(
            url_for(
                "profile.view_profile"
            )
        )

    if request.method == "GET":
        form.full_name.data = (
            current_user.full_name or ""
        )

        form.phone.data = (
            current_user.phone or ""
        )

        form.bio.data = (
            current_user.bio or ""
        )

    return render_template(
        "profile/edit_profile.html",
        form=form
    )