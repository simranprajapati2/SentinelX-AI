import re


def analyze_pdf(text):

    text = text.lower()

    suspicious_words = [
        "pay registration fee",
        "registration fee",
        "processing fee",
        "security deposit",
        "send money",
        "bank account",
        "urgent payment",
        "investment required",
        "click here to pay"
    ]

    found = []

    for word in suspicious_words:
        if word in text:
            found.append(word)

    # Genuine cases ignore karo
    safe_phrases = [
        "no registration fee",
        "no payment required",
        "no processing fee",
        "free application"
    ]

    for phrase in safe_phrases:
        if phrase in text:
            if "registration fee" in found:
                found.remove("registration fee")
            if "processing fee" in found:
                found.remove("processing fee")

    risk_score = round(
        (len(found) / len(suspicious_words)) * 100,
        2
    )

    return {
        "text": text[:1500],
        "keywords": found,
        "risk_score": risk_score
    }