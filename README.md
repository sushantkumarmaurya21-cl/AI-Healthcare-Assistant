# AI Healthcare Assistant 🏥🤖

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge&logo=streamlit)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge&logo=scikit-learn)
![AI](https://img.shields.io/badge/Artificial-Intelligence-purple?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-orange?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Active-success?style=for-the-badge)

</p>

---

## 🌟 Overview

An intelligent AI-powered healthcare assistant that predicts diseases from symptoms, provides precautions, specialist recommendations, voice interaction, report generation, and an interactive chatbot using Machine Learning, NLP, and Streamlit.

---

# ✨ Features

- ✅ Disease Prediction using Machine Learning
- ✅ Symptom-based diagnosis
- ✅ AI Chatbot Assistant
- ✅ Voice Assistant Support
- ✅ Disease Description & Precautions
- ✅ Specialist Recommendation System
- ✅ PDF Report Generation
- ✅ SHAP Explainability
- ✅ Modern Healthcare UI
- ✅ Streamlit Frontend
- ✅ Flask/FastAPI Backend Ready
- ✅ Docker Support
- ✅ NLP Symptom Extraction
- ✅ Authentication Module
- ✅ Responsive Design

---

# 🧠 Technologies Used

## 🚀 Programming
- Python

## 🤖 Machine Learning
- Scikit-learn
- XGBoost
- Random Forest
- Voting Classifier

## 🗣️ NLP
- NLTK
- spaCy

## 🎨 Frontend
- Streamlit
- HTML/CSS

## ⚙️ Backend
- Flask / FastAPI

## 📊 Explainability
- SHAP

## 🗄️ Database
- SQLite

## ☁️ Deployment
- Docker
- GitHub

---

# 📂 Project Structure

```bash
AI_Healthcare_Assistant/
│
├── app/
│   ├── streamlit_app.py
│   ├── components.py
│   ├── chatbot.py
│   ├── report_generator.py
│   ├── voice_assistant.py
│   ├── styles.css
│   └── utils.py
│
├── backend/
│   ├── api.py
│   ├── database.py
│   └── auth.py
│
├── models/
│   ├── train_model.py
│   ├── predict.py
│   ├── evaluate_model.py
│   ├── ensemble_model.pkl
│   ├── label_encoder.pkl
│   └── symptom_columns.pkl
│
├── nlp/
│   ├── symptom_extractor.py
│   └── symptom_standardizer.py
│
├── preprocessing/
│   ├── clean_data.py
│   ├── merge_datasets.py
│   └── feature_engineering.py
│
├── shap_explainability/
│   └── shap_analysis.py
│
├── data/
│   ├── Training.csv
│   ├── Testing.csv
│   ├── symptom_Description.csv
│   ├── symptom_precaution.csv
│   ├── symptom_severity.csv
│   ├── disease_specialist.csv
│   └── healthcare_dataset.csv
│
├── reports/
│   └── generated_reports/
│
├── assets/
│   ├── bg.jpg
│   ├── doctor.png
│   └── logo.png
│
├── requirements.txt
├── Dockerfile
├── README.md
└── setup_commands.txt
```

---

# 📊 Dataset Used

The project uses:

- Disease symptom dataset
- Symptom severity dataset
- Disease precautions dataset
- Disease description dataset
- Healthcare records dataset

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/someshvermagithub/AI-Healthcare-Assistant.git
cd AI_Healthcare_Assistant
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🚀 Run Project

## Step 1 — Train Model

```bash
python models/train_model.py
```

This generates:

- ensemble_model.pkl
- label_encoder.pkl
- symptom_columns.pkl

---

## Step 2 — Run Streamlit App

```bash
streamlit run app/streamlit_app.py
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t ai-healthcare .
```

## Run Docker Container

```bash
docker run -p 8501:8501 ai-healthcare
```

---

# 🧪 Machine Learning Workflow

```text
Dataset → Preprocessing → Feature Engineering →
Model Training → Ensemble Learning →
Prediction → Explainability → Deployment
```

---

# 🤖 AI Features

## 🩺 Disease Prediction

Predicts diseases from symptoms using ensemble ML models.

---

## 🗣️ NLP Symptom Extraction

Extracts symptoms from user text input.

### Example

```text
"I have fever and headache"
```

↓

```text
["fever", "headache"]
```

---

## 🎤 Voice Assistant

Allows voice interaction using speech recognition.

---

## 📈 SHAP Explainability

Explains why a disease prediction was made.

---

# 📸 Recommended Assets

Generate these images using ChatGPT Image Generation:

## 🖼️ Backgrounds

- Doctor background HD
- AI Healthcare futuristic background
- Medical technology wallpaper
- Hospital dashboard UI background

## 🎨 PNG Assets

- AI doctor
- Medical logo
- Healthcare robot assistant
- Stethoscope icon

---

# 🧾 requirements.txt

```txt
streamlit
pandas
numpy
scikit-learn
xgboost
joblib
matplotlib
seaborn
shap
nltk
spacy
SpeechRecognition
pyttsx3
fpdf
flask
uvicorn
fastapi
```

---

# 🐳 Dockerfile

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Your Python 3.10.11 is perfectly compatible.

---

# 📌 GitHub Topics

Add these in your GitHub repository:

```text
machine-learning
healthcare
streamlit
python
artificial-intelligence
nlp
flask
disease-prediction
ai-healthcare
medical-ai
healthcare-chatbot
```

Go to:

```text
Repository → About Section → ⚙️ Settings Icon → Topics
```

---

# 🛠️ Common Errors

## ❌ Error

```python
from models.predict import predict_disease
```

## ✅ Fix

Run this first:

```bash
python models/train_model.py
```

Because model `.pkl` files are not created yet.

---

# 📈 Future Improvements

- 🔹 Deep Learning Integration
- 🔹 RAG-based Medical Chatbot
- 🔹 Doctor Appointment Booking
- 🔹 Medical OCR
- 🔹 Multi-language Support
- 🔹 Real-time Health Monitoring
- 🔹 Firebase Authentication
- 🔹 Cloud Deployment (AWS/GCP/Azure)

---

# 📄 License

MIT License

---

# 👨‍💻 Author

### Developed by Somesh Verma



---

# ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork the repository
- 🧠 Contribute to improvements

---

# 📬 Contact

LinkedIn: https://www.linkedin.com/in/someshverma-/


