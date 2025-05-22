import time
from scripts.train_model import train_model

def simulate_stream():
    model, X = train_model()

    print(" Starting transaction stream...")
    for i, row in X.iterrows():
        data = row.values.reshape(1, -1)
        score = model.decision_function(data)[0]
        result = "FRAUD " if score < 0 else "LEGIT "
        print(f"Transaction {i}: Score={score:.4f} → {result}")
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_stream()
