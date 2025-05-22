import shap
import matplotlib.pyplot as plt

#  Make sure this import is here
from scripts.train_model import train_model

def explain_model():
    model, X = train_model()

    # Only explain a sample to reduce load time
    explainer = shap.Explainer(model.predict, X.sample(100))
    shap_values = explainer(X.sample(100))

    # Visualization
    shap.plots.beeswarm(shap_values)

if __name__ == "__main__":
    explain_model()
