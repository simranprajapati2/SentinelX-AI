from extensions import db
from datetime import datetime


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
)

    activity = db.Column(
        db.Text,
        nullable=False
    )

    ip_address = db.Column(
        db.String(100)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )