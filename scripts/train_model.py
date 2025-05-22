from sklearn.ensemble import IsolationForest
from scripts.preprocess import load_and_clean_data

def train_model():
    df = load_and_clean_data()
    X = df.drop(columns=[
        "TransactionID", "AccountID", "TransactionDate",
        "IP Address", "DeviceID", "MerchantID"
    ], errors='ignore')

    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    model.fit(X)

    return model, X

if __name__ == "__main__":
    model, X = train_model()
    print(" Model trained.")
