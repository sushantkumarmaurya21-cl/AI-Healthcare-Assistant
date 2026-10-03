import shap
import joblib
import pandas as pd

model = joblib.load("models/ensemble_model.pkl")

X = pd.read_csv("data/Training.csv").drop("prognosis", axis=1)

explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X)