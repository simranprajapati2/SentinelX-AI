import os

from flask import (
    Blueprint,
    render_template,
    request,
    current_app
)

from flask_login import login_required

from utils.ocr_utils import (
    extract_text_from_image
)

ocr = Blueprint(
    "ocr",
    __name__,
    url_prefix="/ocr"
)


@ocr.route(
    "/",
    methods=["GET", "POST"]
)
@login_required
def image_ocr():

    result = None

    if request.method == "POST":

        file = request.files.get(
            "image_file"
        )

        if file:

            upload_folder = os.path.join(
                current_app.root_path,
                "uploads",
                "ocr_images"
            )

            os.makedirs(
                upload_folder,
                exist_ok=True
            )

            file_path = os.path.join(
                upload_folder,
                file.filename
            )

            file.save(file_path)

            text = extract_text_from_image(
                file_path
            )

            suspicious_words = [
                "pay fee",
                "send money",
                "registration fee",
                "investment",
                "bank account",
                "urgent payment",
                "click here"
            ]

            found = []

            for word in suspicious_words:
                if word.lower() in text.lower():
                    found.append(word)

            risk_score = (
                len(found)
                / len(suspicious_words)
            ) * 100

            result = {
                "text": text,
                "keywords": found,
                "risk_score": round(
                    risk_score,
                    2
                )
            }

    return render_template(
        "ocr/ocr.html",
        result=result
    )