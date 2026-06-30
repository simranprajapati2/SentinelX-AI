from models.prediction_history import PredictionHistory
from flask import Blueprint, render_template, request
from extensions import db
from ai_model.predictor import predict_job
from models.prediction_history import PredictionHistory
from flask_login import (
login_required,
current_user
)

from ai_model.predictor import predict_job
from services.log_service import create_log

fraud = Blueprint(
"fraud",
__name__,
url_prefix="/fraud"
)

@fraud.route("/", methods=["GET", "POST"])
@login_required
def detect():

    result = None

    if request.method == "POST":

        text = request.form.get("job_text")

        if text:

            prediction, probability = predict_job(text)

            result = {
                "prediction": "Fraud" if prediction == 1 else "Genuine",
                "fraud_score": round(max(probability) * 100, 2)
            }

            history = PredictionHistory(
                user_id=current_user.id,
                input_text=text,
                prediction=result["prediction"],
                confidence=result["fraud_score"]
            )

            db.session.add(history)
            db.session.commit()

            create_log(
                current_user.id,
                "Job Fraud Analysis Performed"
            )

    return render_template(
        "fraud/job_fraud.html",
        result=result
    )