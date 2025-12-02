import pandas as pd
import os

def generate_summary(input_path="data/sentiment_reviews.csv",
                     output_path="data/summary_tables.csv"):

    df = pd.read_csv(input_path)

    # --- Fix: rating column is actually "score" ---
    if "score" not in df.columns:
        raise ValueError("Expected 'score' column not found. Available columns: " + str(df.columns.tolist()))

    # --- Summary tables ---
    summary = {
        "total_reviews": len(df),
        "avg_rating": df["score"].mean(),
        "rating_distribution": df["score"].value_counts().to_dict(),
        "reviews_per_bank": df["bank"].value_counts().to_dict(),
        "sentiment_counts": df["sentiment_label"].value_counts().to_dict() if "sentiment_label" in df.columns else {}
    }

    # Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pd.DataFrame([summary]).to_csv(output_path, index=False)

    print("✔ Summary tables saved to:", output_path)

if __name__ == "__main__":
    generate_summary()

