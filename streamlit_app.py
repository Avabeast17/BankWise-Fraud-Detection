import streamlit as st
from scripts.train_model import train_model
import pandas as pd

st.title("🔐 BankWise: Real-Time Fraud Detection")

model, X = train_model()

st.write("🔎 Example Transaction Risk")
sample = X.sample(1)
score = model.decision_function(sample)[0]

st.dataframe(sample)
st.markdown(f"### ⚠️ Risk Score: `{score:.4f}` → {'FRAUD' if score < 0 else 'LEGIT'}")
