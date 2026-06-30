import os

from flask import (
    Blueprint,
    render_template,
    request,
    current_app
)

from flask_login import login_required
from services.notification_service import create_notification
from utils.pdf_utils import extract_pdf_text
from services.pdf_service import analyze_pdf

pdf = Blueprint(
    "pdf",
    __name__,
    url_prefix="/pdf"
)


@pdf.route(
    "/",
    methods=["GET", "POST"]
)
@login_required
def analyzer():

    result = None

    if request.method == "POST":

        file = request.files.get("pdf_file")

        if file and file.filename.endswith(".pdf"):

            upload_folder = os.path.join(
                current_app.root_path,
                "uploads",
                "pdfs"
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

            text = extract_pdf_text(
                file_path
            )

            result = analyze_pdf(text)
            

    return render_template(
        "pdf/pdf_analyzer.html",
        result=result
    )
