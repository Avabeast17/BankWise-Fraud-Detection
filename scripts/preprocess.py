import pandas as pd

def load_and_clean_data(path="data/bank_transactions.csv"):
    df = pd.read_csv(path)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Encode categorical columns
    for col in df.select_dtypes(include=['object', 'category']).columns:
        df[col] = df[col].astype('category').cat.codes

    return df

if __name__ == "__main__":
    df = load_and_clean_data()
    print(df.info())
    print(df.head())
