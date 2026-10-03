import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
train_df = pd.read_csv("data/Training.csv")

# Features and target
X = train_df.drop("prognosis", axis=1)
y = train_df["prognosis"]

# Label encoding
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, pred)
print(f"Accuracy: {acc}")

# Save model
joblib.dump(model, "models/ensemble_model.pkl")
joblib.dump(encoder, "models/label_encoder.pkl")
joblib.dump(list(X.columns), "models/symptom_columns.pkl")

print("Model Saved Successfully")