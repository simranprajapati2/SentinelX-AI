from flask import (
    Blueprint,
    render_template
)

from flask_login import (
    login_required,
    current_user
)

from models.activity_log import (
    ActivityLog
)

logs = Blueprint(
    "logs",
    __name__,
    url_prefix="/logs"
)


@logs.route("/")
@login_required
def activity_logs():

    activities = ActivityLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        ActivityLog.id.desc()
    ).all()

    return render_template(
        "logs/activity_logs.html",
        activities=activities
    )