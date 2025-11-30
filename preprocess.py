import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw_reviews.csv")

# ---- CLEANING ----

# Remove duplicates based on the review text column
df.drop_duplicates(subset=["content"], inplace=True)

# Remove rows where review text is missing
df.dropna(subset=["content"], inplace=True)

# Convert date column to YYYY-MM-DD
df["at"] = pd.to_datetime(df["at"], errors="coerce").dt.date

# Keep only the important columns for analysis
df_clean = df[[
    "review_id",
    "bank",
    "app_name",
    "score",
    "content",
    "at",
    "source"
]]

# Save cleaned dataset
df_clean.to_csv("data/clean_reviews.csv", index=False)

print("Cleaning complete! File saved: data/clean_reviews.csv")

