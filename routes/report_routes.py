import os
from flask import render_template
from flask import Blueprint, send_file, render_template, redirect, url_for, flash
from flask import (
    Blueprint,
    send_file
)
from services.notification_service import create_notification
from flask_login import (
    login_required,
    current_user
)

from models.report import Report
from extensions import db
from services.report_service import generate_report

report = Blueprint(
    "report",
    __name__,
    url_prefix="/reports"
)


@report.route("/")
@login_required
def generate():

    os.makedirs(
        "uploads/reports",
        exist_ok=True
    )

    filename = (
        f"report_{current_user.id}.xlsx"
    )

    path = os.path.join(
        "uploads/reports",
        filename
    )

    generate_report(
        path,
        current_user.username
    )

    saved_report = Report(
        user_id=current_user.id,
        report_name=filename,
        report_path=path
    )

    db.session.add(saved_report)
    create_notification(
    current_user.id,
    "Report Generated",
    "Your report has been generated successfully."
)
    db.session.commit()

    return send_file(
        path,
        as_attachment=True
    )
@report.route("/history")
@login_required
def history():

    reports = Report.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Report.id.desc()
    ).all()

    return render_template(
        "reports/history.html",
        reports=reports
    )
@report.route("/download/<int:report_id>")
@login_required
def download(report_id):

    report = Report.query.get_or_404(report_id)

    if report.user_id != current_user.id:
        return "Access Denied", 403

    if not os.path.exists(report.report_path):
        return "File not found", 404

    return send_file(
        report.report_path,
        as_attachment=True
    )

@report.route("/delete/<int:report_id>")
@login_required
def delete(report_id):

    report = Report.query.get_or_404(report_id)

    if report.user_id != current_user.id:
        return "Access Denied", 403

    if os.path.exists(report.report_path):
        os.remove(report.report_path)

    db.session.delete(report)
    db.session.commit()

    return redirect( url_for("report.history")
    )