from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    jsonify,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from models.notification import Notification
from extensions import db


notification = Blueprint(
    "notification",
    __name__,
    url_prefix="/notifications"
)


@notification.route("/")
@login_required
def index():

    notifications = (
        Notification.query
        .filter_by(
            user_id=current_user.id
        )
        .order_by(
            Notification.created_at.desc()
        )
        .all()
    )

    return render_template(
        "notifications/notifications.html",
        notifications=notifications
    )


@notification.route("/read/<int:id>")
@login_required
def mark_read(id):

    note = Notification.query.get_or_404(id)

    if note.user_id != current_user.id:
        return redirect(
            url_for("notification.index")
        )

    note.is_read = True
    db.session.commit()

    return redirect(
        url_for("notification.index")
    )
@notification.route("/count")
@login_required
def count():

    unread = Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).count()

    return jsonify({
        "count": unread
    })
@notification.route("/api")
@login_required
def api():

    notifications = (
        Notification.query
        .filter_by(user_id=current_user.id)
        .order_by(Notification.created_at.desc())
        .all()
    )

    return jsonify([
        {
            "id": n.id,
            "title": n.title or "Notification",
            "message": n.message,
            "is_read": n.is_read,
            "created_at":
            n.created_at.strftime("%d-%m-%Y %H:%M")
        }
        for n in notifications
    ])
@notification.route("/read-all")
@login_required
def read_all():

    notifications = Notification.query.filter_by(
        user_id=current_user.id,
        is_read=False
    ).all()

    for n in notifications:
        n.is_read = True

    db.session.commit()

    return redirect(
        url_for("notification.index")
    )
@notification.route("/delete/<int:id>")
@login_required
def delete(id):

    note = Notification.query.get_or_404(id)

    if note.user_id != current_user.id:
        return redirect(
            url_for("notification.index")
        )

    db.session.delete(note)
    db.session.commit()

    flash(
        "Notification deleted successfully.",
        "success"
    )

    return redirect(
        url_for("notification.index")
    )