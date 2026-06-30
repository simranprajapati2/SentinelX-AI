import random
from datetime import datetime, timedelta
from flask import session, request
from models.otp_code import OTPCode
from services.email_service import send_email
from services.log_service import create_log
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from services.notification_service import create_notification
from extensions import db
from models.user import User
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request,
    session
)

# Optional imports
try:
    from models.report import Report
except ImportError:
    Report = None

try:
    from models.activity_log import ActivityLog
except ImportError:
    ActivityLog = None


admin = Blueprint("admin", __name__, url_prefix="/admin")


# ==========================
# Admin Permission Check
# ==========================
def admin_required():
    if not current_user.is_admin:
        flash("Access Denied", "danger")
        return False
    return True


@login_required
def verify_otp():

    if request.method == "POST":

        entered_otp = request.form.get("otp")

        otp = OTPCode.query.filter_by(
            user_id=current_user.id
        ).first()

        if not otp:
            flash("OTP not found", "danger")
            return redirect(
                url_for("admin.verify_admin")
            )

        if otp.expires_at < datetime.utcnow():
            flash("OTP expired", "danger")
            return redirect(
                url_for("admin.verify_admin")
            )

        if otp.otp_code != entered_otp:
            flash("Invalid OTP", "danger")
            return redirect(
                url_for("admin.verify_otp")
            )

        db.session.delete(otp)

        current_user.admin_verified = True

        db.session.commit()

        return redirect(
            url_for("admin.dashboard")
        )

    return render_template(
        "admin/admin_otp.html"
    )
# ==========================
# Admin Dashboard
# ==========================
@admin.route("/")
@login_required
def dashboard():

    if not current_user.is_admin:
        return redirect(
            url_for("dashboard.home")
        )

    session["admin_verified"] = False

    return redirect(
        url_for("admin.verify_admin")
    )
# ==========================
# View Users
# ==========================
@admin.route("/users")
@login_required
def users():
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    all_users = User.query.all()

    return render_template("admin/users.html", users=all_users)


# ==========================
# Block User
# ==========================
@admin.route("/block/<int:user_id>")
@login_required
def block_user(user_id):
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    user = User.query.get_or_404(user_id)
    user.is_blocked = True
    create_notification(
        user.id,
        "Account Blocked",
        "Your account has been blocked by the administrator."
    )

    db.session.commit()
    

    flash("User blocked successfully.", "success")
    return redirect(url_for("admin.users"))


# ==========================
# Unblock User
# ==========================
@admin.route("/unblock/<int:user_id>")
@login_required
def unblock_user(user_id):
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    user = User.query.get_or_404(user_id)
    user.is_blocked = False
    create_notification(
    user.id,
    "Account Unblocked",
    "Your account has been unblocked."
)

    db.session.commit()

    flash("User unblocked successfully.", "success")
    return redirect(url_for("admin.users"))


# ==========================
# Delete User
# ==========================
@admin.route("/delete-user/<int:user_id>")
@login_required
def delete_user(user_id):
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash("You cannot delete your own account.", "danger")
        return redirect(url_for("admin.users"))

    create_log(current_user.id, f"Deleted User {user.email}")

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")
    return redirect(url_for("admin.users"))


# ==========================
# Reports
# ==========================
@admin.route("/reports")
@login_required
def reports():
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    reports = Report.query.all() if Report else []

    return render_template("admin/reports.html", reports=reports)


# ==========================
# Activity Logs
# ==========================
@admin.route("/logs")
@login_required
def logs():
    if not admin_required():
        return redirect(url_for("dashboard.home"))

    logs = (
        ActivityLog.query.order_by(ActivityLog.id.desc()).all()
        if ActivityLog else []
    )

    return render_template("admin/logs.html", logs=logs)


# ==========================
# Unlock User 
# ==========================
@admin.route("/unlock/<int:user_id>")
@login_required
def unlock_user(user_id):

    if not admin_required():
        return redirect(
            url_for("dashboard.home")
        )

    user = User.query.get_or_404(user_id)

    user.is_locked = False
    user.failed_login_attempts = 0
    user.locked_until = None

    db.session.commit()

    create_log(
        current_user.id,
        f"Unlocked account: {user.email}"
    )

    flash(
        f"{user.email} account unlocked successfully.",
        "success"
    )

    return redirect(
        url_for("admin.users")
    )


@admin.route(
    "/verify-admin",
    methods=["GET", "POST"]
)
@login_required
def verify_admin():

    if not current_user.is_admin:
        return redirect(
            url_for("dashboard.home")
        )

    otp = OTPCode.query.filter_by(
        user_id=current_user.id
    ).first()

    # GET request
    if request.method == "GET":

        if otp:
            db.session.delete(otp)
            db.session.commit()

        otp_code = str(
            random.randint(100000, 999999)
        )

        otp = OTPCode(
            user_id=current_user.id,
            otp_code=otp_code,
            expires_at=datetime.utcnow()
            + timedelta(minutes=5)
        )

        db.session.add(otp)
        db.session.commit()

        send_email(
            subject="SentinelX AI Admin OTP",
            recipients=[current_user.email],
            body=f"""
Hello {current_user.username},

Your Admin OTP is:

{otp_code}

This OTP is valid for 5 minutes.

SentinelX AI Team
"""
        )

        return render_template(
            "admin/verify_admin.html"
        )

    # POST request
    entered_otp = request.form.get("otp")

    otp = OTPCode.query.filter_by(
        user_id=current_user.id
    ).first()

    if not otp:
        flash(
            "OTP not found.",
            "danger"
        )
        return redirect(
            url_for("admin.verify_admin")
        )

    if otp.expires_at < datetime.utcnow():

        db.session.delete(otp)
        db.session.commit()

        flash(
            "OTP expired.",
            "danger"
        )

        return redirect(
            url_for("admin.verify_admin")
        )

    if entered_otp != otp.otp_code:

        flash(
            "Invalid OTP.",
            "danger"
        )

        return redirect(
            url_for("admin.verify_admin")
        )

    db.session.delete(otp)

    session["admin_verified"] = True

    db.session.commit()

    flash(
        "Admin verification successful.",
        "success"
    )

    return redirect(
        url_for("admin.panel")
    )




@admin.route("/resend-admin-otp")
@login_required
def resend_admin_otp():

    otp = OTPCode.query.filter_by(
        user_id=current_user.id
    ).first()

    if otp:
        db.session.delete(otp)
        db.session.commit()

    otp_code = str(
        random.randint(100000, 999999)
    )

    otp = OTPCode(
        user_id=current_user.id,
        otp_code=otp_code,
        expires_at=datetime.utcnow()
        + timedelta(minutes=5)
    )

    db.session.add(otp)
    db.session.commit()

    send_email(
        subject="SentinelX AI Admin Verification OTP",
        recipients=[current_user.email],
        body=f"""
Hello {current_user.username},

Your new Admin OTP is:

{otp_code}

This OTP is valid for 5 minutes.
"""
    )

    flash(
        "New OTP sent successfully.",
        "success"
    )

    return redirect(
        url_for("admin.verify_admin")
    )
@admin.route("/panel")
@login_required
def panel():

    if not current_user.is_admin:
        return redirect(
            url_for("dashboard.home")
        )

    if not session.get("admin_verified"):
        flash(
            "Please verify OTP first.",
            "danger"
        )
        return redirect(
            url_for("admin.verify_admin")
        )

    total_users = User.query.count()
    total_reports = Report.query.count() if Report else 0
    total_logs = ActivityLog.query.count() if ActivityLog else 0

    return render_template(
        "admin/admin_dashboard.html",
        total_users=total_users,
        total_reports=total_reports,
        total_logs=total_logs
    )