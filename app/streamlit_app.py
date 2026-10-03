import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

import streamlit as st

from models.predict import predict_disease

from models.predict import predict_disease
from app.utils import (
    get_description,
    get_precautions,
    get_specialist
)
from app.report_generator import generate_report

st.set_page_config(page_title="AI Healthcare Assistant")

st.title("AI Healthcare Assistant")

name = st.text_input("Enter Patient Name")

symptoms = st.text_area(
    "Enter Symptoms separated by comma"
)

if st.button("Predict Disease"):

    symptom_list = [s.strip() for s in symptoms.split(",")]

    disease = predict_disease(symptom_list)

    description = get_description(disease)

    precautions = get_precautions(disease)

    specialist = get_specialist(disease)

    st.success(f"Predicted Disease: {disease}")

    st.subheader("Disease Description")
    st.write(description)

    st.subheader("Recommended Specialist")
    st.write(specialist)

    st.subheader("Precautions")

    for p in precautions:
        st.write(f"✔ {p}")

    report_path = generate_report(
        name,
        disease,
        description,
        precautions
    )

    with open(report_path, "rb") as file:
        st.download_button(
            label="Download Report",
            data=file,
            file_name="health_report.pdf",
            mime="application/pdf"
        )