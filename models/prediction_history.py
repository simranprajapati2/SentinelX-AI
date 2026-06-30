from extensions import db
from datetime import datetime


class PredictionHistory(db.Model):
    __tablename__ = "prediction_history"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    input_text = db.Column(
        db.Text,
        nullable=False
    )

    prediction = db.Column(
        db.String(50)
    )

    confidence = db.Column(
        db.Float
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )