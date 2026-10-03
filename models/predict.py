import joblib
import pandas as pd

model = joblib.load("models/ensemble_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")
columns = joblib.load("models/symptom_columns.pkl")


def predict_disease(symptoms):
    input_data = [0] * len(columns)

    for symptom in symptoms:
        symptom = symptom.strip()

        if symptom in columns:
            index = columns.index(symptom)
            input_data[index] = 1

    input_df = pd.DataFrame([input_data], columns=columns)

    prediction = model.predict(input_df)[0]

    disease = encoder.inverse_transform([prediction])[0]
    print("It runned")

    return disease