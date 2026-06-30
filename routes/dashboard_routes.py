from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard.route("/")
@login_required
def home():

    stats = {
        "reports": 18,
        "threats": 7,
        "safe_sites": 120,
        "notifications": 5
    }

    activities = [
        "PDF Scam Analysis Completed",
        "New Login from Chrome",
        "Website Verification Completed",
        "OCR Scan Finished"
    ]

    return render_template(
        "dashboard/dashboard.html",
        stats=stats,
        activities=activities,
        user=current_user
    )