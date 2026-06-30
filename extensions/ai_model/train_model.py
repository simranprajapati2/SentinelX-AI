import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv(
"ai_model/job_dataset.csv"
)

X = df["text"]
y = df["label"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

joblib.dump(
model,
"ai_model/phishing_model.pkl"
)

joblib.dump(
vectorizer,
"ai_model/vectorizer.pkl"
)

print("Model Trained Successfully")
