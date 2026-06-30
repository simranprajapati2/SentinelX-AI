from flask_wtf import FlaskForm
from flask_wtf.file import (
    FileField,
    FileAllowed
)

from wtforms import (
    StringField,
    TextAreaField,
    SubmitField
)


class ProfileForm(FlaskForm):

    full_name = StringField(
        "Full Name"
    )

    phone = StringField(
        "Phone"
    )

    bio = TextAreaField(
        "Bio"
    )

    profile_image = FileField(
        "Profile Image",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png"],
                "Only JPG and PNG images are allowed."
            )
        ]
    )

    submit = SubmitField(
        "Update Profile"
    )