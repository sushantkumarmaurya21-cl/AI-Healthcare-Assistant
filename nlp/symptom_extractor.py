import re


def extract_symptoms(text):
    text = text.lower()

    symptoms = re.split(r',|and', text)

    return [s.strip().replace(' ', '_') for s in symptoms]