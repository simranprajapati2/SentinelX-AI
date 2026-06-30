import joblib

model = joblib.load(
    "ai_model/phishing_model.pkl"
)

vectorizer = joblib.load(
    "ai_model/vectorizer.pkl"
)


def predict_job(text):

    data = vectorizer.transform(
        [text]
    )

    prediction = model.predict(
        data
    )[0]

    probability = model.predict_proba(
        data
    )[0]

    return prediction, probability