
from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for
)

from flask_login import (
    login_required
)

from services.backup_service import (
    create_backup
)

from models.user import User
from models.report import Report
from models.activity_log import ActivityLog


database = Blueprint(
    "database",
    __name__,
    url_prefix="/database"
)


# ==========================
# Database Dashboard
# ==========================
@database.route("/")
@login_required
def dashboard():

    return render_template(
        "database/dashboard.html"
    )


# ==========================
# Create Backup
# ==========================
@database.route("/backup")
@login_required
def backup():

    try:
        filename = create_backup()

        flash(
            f"Backup created successfully: {filename}",
            "success"
        )

    except Exception as e:

        flash(
            f"Backup failed: {str(e)}",
            "danger"
        )

    return redirect(
        url_for("database.dashboard")
    )


# ==========================
# Database Statistics
# ==========================
@database.route("/stats")
@login_required
def stats():

    total_users = User.query.count()
    total_reports = Report.query.count()
    total_logs = ActivityLog.query.count()

    return render_template(
        "database/stats.html",
        total_users=total_users,
        total_reports=total_reports,
        total_logs=total_logs
    )

