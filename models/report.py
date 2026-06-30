from extensions import db
from datetime import datetime


class Report(db.Model):

    __tablename__ = "reports"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),   # ADD THIS
        nullable=False
    )

    report_name = db.Column(
        db.String(255),
        nullable=False
    )

    report_path = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )