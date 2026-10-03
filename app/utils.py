import pandas as pd


def get_description(disease):
    df = pd.read_csv("data/symptom_Description.csv", header=None)

    for index, row in df.iterrows():
        if row[0].strip() == disease:
            return row[1]

    return "No Description Found"



def get_precautions(disease):
    df = pd.read_csv("data/symptom_precaution.csv", header=None)

    for index, row in df.iterrows():
        if row[0].strip() == disease:
            return row[1:].dropna().tolist()

    return []



def get_specialist(disease):
    df = pd.read_csv("data/disease_specialist.csv")

    result = df[df["Disease"] == disease]

    if len(result) > 0:
        return result.iloc[0]["Specialist"]

    return "General Physician"