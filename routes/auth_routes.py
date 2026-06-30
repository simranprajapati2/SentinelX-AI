from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
    request
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from flask_mail import Message

from extensions import (
    db,
    bcrypt,
    mail
)
from services.notification_service import create_notification
from models.user import User
from models.password_reset_token import PasswordResetToken
from models.otp_code import OTPCode
from middleware.rate_limiter import is_rate_limited
from forms.login_form import LoginForm
from forms.register_form import RegisterForm

from services.email_service import send_email
from services.password_validator import validate_password
import secrets
import random
from datetime import datetime, timedelta
from services.log_service import (
    create_log
)

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)
@auth.route("/register", methods=["GET", "POST"])
def register():


 form = RegisterForm()

 if form.validate_on_submit():

    # Check existing email
    user = User.query.filter_by(
        email=form.email.data
    ).first()

    if user:
        flash(
            "Email already exists.",
            "danger"
        )
        return redirect(
            url_for("auth.register")
        )

    # Check existing username
    existing_username = User.query.filter_by(
        username=form.username.data
    ).first()

    if existing_username:
        flash(
            "Username already exists.",
            "danger"
        )
        return redirect(
            url_for("auth.register")
        )

    # Hash password
    hashed_password = bcrypt.generate_password_hash(
        form.password.data
    ).decode("utf-8")

    # Generate verification token
    token = secrets.token_urlsafe(32)

    # Create user
    new_user = User(
        username=form.username.data,
        full_name=form.full_name.data,
        email=form.email.data,
        password_hash=hashed_password,
        email_verified=False,
        verification_token=token
    )

    db.session.add(new_user)
    db.session.commit()
    create_notification(
    new_user.id,
    "Welcome",
    "Welcome to SentinelX AI."
)

    # Email verification link
    verification_link = url_for(
        "auth.verify_email",
        token=token,
        _external=True
    )

    send_email(
        subject="Verify Your SentinelX AI Account",
        recipients=[new_user.email],
        body=f"""


 Hello {new_user.full_name},

 Please verify your email:

 {verification_link}

 Thank you,
 SentinelX AI Team
 """
)


    flash(
        "Registration successful. Please verify your email.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )

 return render_template(
    "auth/register.html",
    form=form
)



from flask import request

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(
            email=email
        ).first()

        # User not found
        if not user:
            flash(
                "Invalid email or password.",
                "danger"
            )
            return redirect(
                url_for("auth.login")
            )

        # Account blocked
        if user.is_blocked:
            flash(
                "Your account has been blocked.",
                "danger"
            )
            return redirect(
                url_for("auth.login")
            )

        # Account locked
        if user.is_locked:

            if (
                user.locked_until and
                datetime.utcnow() >= user.locked_until
            ):
                user.is_locked = False
                user.failed_login_attempts = 0
                user.locked_until = None
                db.session.commit()

            else:
                flash(
                    "Account locked. Try again after 30 minutes.",
                    "danger"
                )
                return redirect(
                    url_for("auth.login")
                )

        # Email verification
        if not user.email_verified:
            flash(
                "Please verify your email first.",
                "warning"
            )
            return redirect(
                url_for("auth.login")
            )

        # Correct password
        if bcrypt.check_password_hash(
            user.password_hash,
            password
        ):

            user.failed_login_attempts = 0
            user.is_locked = False
            user.locked_until = None
            user.last_login = datetime.utcnow()

            db.session.commit()

            login_user(user)

            create_log(
                user.id,
                "User Logged In"
            )
            create_notification(
    user.id,
    "Login Successful",
    "You logged in successfully."
)
            db.session.commit()

            flash(
                "Login successful.",
                "success"
            )

            return redirect(
                url_for("dashboard.home")
            )

        # Wrong password
        user.failed_login_attempts += 1
        create_notification(
    user.id,
    "Security Alert",
    "Failed login attempt detected."
)

        create_log(
            user.id,
            "Failed Login Attempt"
        )
        db.session.commit()

        if user.failed_login_attempts >= 5:

            user.is_locked = True
            create_notification(
    user.id,
    "Account Locked",
    "Your account has been locked for 30 minutes."
)
            user.locked_until = (
                datetime.utcnow()
                + timedelta(minutes=30)
            )
            db.session.commit()

            create_log(
    user.id,
    "Failed Login Attempt"
)
            db.session.commit()

            create_log(
                user.id,
                "Account Locked"
            )
            db.session.commit()

            flash(
                "Account locked for 30 minutes.",
                "danger"
            )

        db.session.commit()

        flash(
            "Invalid email or password.",
            "danger"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/login.html"
    )


from flask import session

@auth.route("/logout")
@login_required
def logout():

    create_log(
        current_user.id,
        "User Logged Out"
    )

    current_user.admin_verified = False
    db.session.commit()

    # Admin OTP session remove
    session.pop(
        "admin_verified",
        None
    )

    logout_user()

    return redirect(
        url_for("auth.login")
    )

# =========================

# Forgot Password

# =========================

@auth.route(

    "/forgot-password",

    methods=["GET", "POST"]

)

def forgot_password():



    if request.method == "POST":



        email = request.form.get(

            "email"

        )



        user = User.query.filter_by(

            email=email

        ).first()



        if user:



            token = secrets.token_urlsafe(32)



            reset = PasswordResetToken(

                user_id=user.id,

                token=token,

                expires_at=datetime.utcnow()

                + timedelta(hours=1)

            )



            db.session.add(reset)

            db.session.commit()



            link = url_for(

                "auth.reset_password",

                token=token,

                _external=True

            )



            msg = Message(

                "Password Reset",

                recipients=[user.email]

            )



            msg.body = f"""

Reset your password:



{link}



This link expires in 1 hour.

"""



            mail.send(msg)



        flash(

            "If the email exists, a reset link has been sent.",

            "info"

        )



        return redirect(

            url_for("auth.login")

        )



    return render_template(

        "auth/forgot_password.html"

    )





# =========================

# Reset Password

# =========================

@auth.route(
    "/reset-password/<token>",
    methods=["GET", "POST"]
)
def reset_password(token):

    reset = PasswordResetToken.query.filter_by(
        token=token
    ).first()

    if (
        not reset or
        reset.expires_at < datetime.utcnow()
    ):
        flash(
            "Invalid or expired link.",
            "danger"
        )
        return redirect(
            url_for("auth.login")
        )

    if request.method == "POST":

        password = request.form.get(
            "password"
        )

        user = User.query.get(
            reset.user_id
        )

        user.password_hash = (
            bcrypt.generate_password_hash(
                password
            ).decode("utf-8")
        )

        db.session.delete(reset)
        db.session.commit()
        create_notification(
    user.id,
    "Password Changed",
    "Your password has been updated."
)

        flash(
            "Password updated successfully.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/reset_password.html",
        token=token
    )
@auth.route("/verify-email/<token>")
def verify_email(token):

    user = User.query.filter_by(
        verification_token=token
    ).first()

    if not user:
        flash(
            "Invalid verification link.",
            "danger"
        )
        return redirect(
            url_for("auth.login")
        )

    user.email_verified = True
    user.verification_token = None

    db.session.commit()
    create_notification(
    user.id,
    "Email Verified",
    "Your email has been verified successfully."
)

    flash(
        "Email verified successfully. Please login.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )
@auth.route(
    "/resend-verification",
    methods=["GET", "POST"]
)
def resend_verification():

    if request.method == "POST":

        email = request.form.get("email")

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            flash(
                "Email not found.",
                "danger"
            )
            return redirect(
                url_for("auth.resend_verification")
            )

        if user.email_verified:
            flash(
                "Email is already verified.",
                "success"
            )
            return redirect(
                url_for("auth.login")
            )

        token = secrets.token_urlsafe(32)

        user.verification_token = token

        db.session.commit()

        verification_link = url_for(
            "auth.verify_email",
            token=token,
            _external=True
        )

        send_email(
            subject="Verify Your SentinelX AI Account",
            recipients=[user.email],
            body=f"""
Hello {user.username},

Please verify your account:

{verification_link}

SentinelX AI Team
"""
        )

        flash(
            "Verification email sent successfully.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/resend_verification.html"
    )
@auth.route("/resend-otp/<int:user_id>")
def resend_otp(user_id):

    user = User.query.get_or_404(user_id)

    # Purana OTP delete karo
    old_otp = OTPCode.query.filter_by(
        user_id=user.id
    ).first()

    if old_otp:
        db.session.delete(old_otp)
        db.session.commit()

    # Naya OTP generate karo
    otp_code = str(
        random.randint(100000, 999999)
    )

    otp = OTPCode(
        user_id=user.id,
        otp_code=otp_code,
        expires_at=datetime.utcnow()
        + timedelta(minutes=5)
    )

    db.session.add(otp)
    db.session.commit()

    # Email bhejo
    send_email(
        subject="SentinelX AI OTP Verification",
        recipients=[user.email],
        body=f"""
Hello {user.username},

Your new OTP is:

{otp_code}

This OTP is valid for 5 minutes.

SentinelX AI Team
"""
    )

    flash(
        "New OTP sent to your email.",
        "success"
    )

    return redirect(
    url_for(
        "auth.verify_otp",
        user_id=user.id
    )
)
