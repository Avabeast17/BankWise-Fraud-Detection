BankWise — Fraud Detection Using Unsupervised Learning

Overview
In a world where financial fraud is growing more sophisticated, traditional rule-based systems struggle to keep up. BankWise is a real-time anomaly detection project designed to detect suspicious bank transactions using unsupervised learning — no labels, no prior assumptions, just intelligent pattern recognition.
This project simulates how banks can proactively identify potential fraud using Isolation Forest, SHAP explainability, and real transaction behavior.

Problem Statement
Banks deal with thousands of transactions every minute. Hidden within those are anomalies that may indicate fraudulent behavior. Most real-world data is unlabeled, which makes supervised models impractical at scale. The question becomes:
How do you flag high-risk transactions before damage is done even without labeled fraud data?

Solution
I used the Isolation Forest algorithm to detect anomalies across bank transaction features such as amount, login attempts, channel, customer age, and duration. SHAP values provide transparency, allowing teams to understand why a transaction was flagged.
This model:
* Detects fraud-like patterns using only customer behavior.
* Adapts to new, unseen transaction types.
* Provides explainability through SHAP for trust and interpretability.
* Supports real-time detection through simulation-ready code.

Key Features
* Isolation Forest for unsupervised anomaly detection
* SHAP-based explainability to support audit trails
* Powerful EDA visuals to contrast normal vs. anomalous behavior
* CSV output of flagged transactions and feature insights
* Streamlit app for demo and simulation


Out of 2,512 transactions, 51 were flagged as anomalous. Anomalies showed significantly higher login attempts and irregular transaction amounts, especially in non-standard channels like mobile or kiosk.

Why This Matters
* Banks can’t rely on rules alone. Fraudsters adapt quickly.
* Unsupervised models offer a new way forward flagging patterns that break from the norm, even when they’ve never been seen before.
* Explainability matters. Every flagged transaction is backed by feature importance scores.


Final Note
This project is a small window into the future of fraud prevention flexible, explainable, and designed to protect before the damage is done.

