from extensions import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    full_name = db.Column(
        db.String(150)
    )

    phone = db.Column(
        db.String(20)
    )

    bio = db.Column(
        db.Text
    )

    profile_image = db.Column(
        db.String(255),
        default="default.png"
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    email_verified = db.Column(
        db.Boolean,
        default=False
    )

    verification_token = db.Column(
        db.String(255)
    )

    is_admin = db.Column(
        db.Boolean,
        default=False
    )
    admin_verified = db.Column(
    db.Boolean,
    default=False
      )
    admin_otp = db.Column(
    db.String(6)
)

    admin_otp_expiry = db.Column(
    db.DateTime
)

    is_blocked = db.Column(
        db.Boolean,
        default=False
    )

    failed_login_attempts = db.Column(
        db.Integer,
        default=0
    )

    is_locked = db.Column(
        db.Boolean,
        default=False
    )
    locked_until = db.Column(
        db.DateTime,
        nullable=True
    )

    last_login = db.Column(
        db.DateTime
    )
    otp_codes = db.relationship(
    "OTPCode",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    activity_logs = db.relationship(
    "ActivityLog",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    password_reset_tokens = db.relationship(
    "PasswordResetToken",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    notifications = db.relationship(
    "Notification",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)
    reports = db.relationship(
    "Report",
    backref="user",
    lazy=True,
    cascade="all, delete-orphan"
)

    def __repr__(self):
        return f"<User {self.email}>"