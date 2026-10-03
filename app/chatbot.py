from models.predict import predict_disease


def chatbot_response(user_symptoms):
    disease = predict_disease(user_symptoms)

    return f"Predicted Disease: {disease}"