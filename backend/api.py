from flask import Flask, request, jsonify

from models.predict import predict_disease

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    symptoms = data['symptoms']

    disease = predict_disease(symptoms)

    return jsonify({
        'predicted_disease': disease
    })


if __name__ == '__main__':
    app.run(debug=True)