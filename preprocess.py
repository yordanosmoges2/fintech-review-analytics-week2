import pandas as pd

def preprocess_reviews(input_path="data/raw_reviews.csv",
                       output_path="data/clean_reviews.csv"):

    # Load data
    df = pd.read_csv(input_path)

    # ---- FIX 1: Normalize column names ----
    df.columns = df.columns.str.lower().str.strip()

    # ---- FIX 2: Standardize required columns ----
    required_cols = ["review_id", "bank", "app_name", "score",
                     "content", "at", "source"]

    # Warn if required columns missing
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print("Missing required columns:", missing)

    df = df[required_cols]

    # ---- FIX 3: Drop rows with no text ----
    df = df.dropna(subset=["content"])

    # ---- FIX 4: Normalize dates ----
    df["at"] = pd.to_datetime(df["at"], errors="coerce").dt.date

    # ---- FIX 5: Validate ≥ 400 reviews per bank ----
    print("\nReview count per bank:")
    print(df["bank"].value_counts())

    assert df["bank"].value_counts().min() >= 400, \
        "❌ Each bank must have at least 400 reviews!"

    # ---- FIX 6: Save cleaned dataset ----
    df.to_csv(output_path, index=False)
    print("\n✔ Cleaning complete! Saved to:", output_path)


if __name__ == "__main__":
    preprocess_reviews()



