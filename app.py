from flask import Flask, redirect, url_for
from middleware.session_manager import SESSION_TIMEOUT
app = Flask(__name__)
app.permanent_session_lifetime = SESSION_TIMEOUT
from config import Config
from extensions import (
    db,
    bcrypt,
    login_manager,
    mail
)
from routes.auth_routes import auth
from routes.dashboard_routes import dashboard
from routes.profile_routes import profile
from routes.fraud_detection_routes import fraud
from routes.pdf_routes import pdf
from models.user import User
from routes.ocr_routes import ocr
from routes.website_verification_routes import website
from routes.report_routes import report
from routes.notification_routes import notification
from routes.admin_routes import admin
from routes.logs_routes import logs
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.database_routes import database
from models.user import User
from models.report import Report
from models.activity_log import ActivityLog


limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per hour"]
 )

app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
mail.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(profile)
app.register_blueprint(fraud)
app.register_blueprint(pdf)
app.register_blueprint(ocr)
app.register_blueprint(website)
app.register_blueprint(report)

app.register_blueprint(
    notification
)
app.register_blueprint(admin)
app.register_blueprint(logs)
app.permanent_session_lifetime = SESSION_TIMEOUT
app.register_blueprint(database)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(
        User,
        int(user_id)
    )


@app.route("/")
def home():
    return redirect(
        url_for("auth.login")
    )




if __name__ == "__main__":
    app.run(debug=True)