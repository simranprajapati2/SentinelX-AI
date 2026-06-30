import validators
from urllib.parse import urlparse


def check_website(url):

    result = {
        "valid": False,
        "https": False,
        "domain": "",
        "risk_score": 0,
        "warnings": []
    }

    if not validators.url(url):
        result["warnings"].append(
            "Invalid URL"
        )
        return result

    result["valid"] = True

    parsed = urlparse(url)

    domain = parsed.netloc.lower()

    result["domain"] = domain

    if url.startswith("https://"):
        result["https"] = True
    else:
        result["warnings"].append(
            "Website is not using HTTPS"
        )
        result["risk_score"] += 30

    suspicious_words = [
        "login",
        "verify",
        "update",
        "bank",
        "secure",
        "free",
        "bonus",
        "gift"
    ]

    for word in suspicious_words:

        if word in url.lower():

            result["warnings"].append(
                f"Suspicious keyword: {word}"
            )

            result["risk_score"] += 10

    if result["risk_score"] > 100:
        result["risk_score"] = 100

    return result