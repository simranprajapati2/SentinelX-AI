from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    Length
)

class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[DataRequired()]
    )

    full_name = StringField(
        "Full Name",
        validators=[DataRequired()]
    )

    email = StringField(
        "Email",
        validators=[DataRequired()]
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()]
    )

    submit = SubmitField(
        "Register"
    )