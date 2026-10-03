from fpdf import FPDF


def generate_report(patient_name, disease, description, precautions):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="AI Healthcare Report", ln=True, align='C')

    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Patient Name: {patient_name}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Disease: {disease}", ln=True)

    pdf.multi_cell(0, 10, txt=f"Description: {description}")

    pdf.ln(5)

    pdf.cell(200, 10, txt="Precautions:", ln=True)

    for precaution in precautions:
        pdf.cell(200, 10, txt=f"- {precaution}", ln=True)

    filename = f"reports/generated_reports/{patient_name}_report.pdf"

    pdf.output(filename)

    return filename