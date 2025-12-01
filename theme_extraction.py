import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os

def extract_themes(input_path="data/nlp_reviews.csv",
                   output_path="data/themes.csv",
                   top_n=10):

    df = pd.read_csv(input_path)

    # Make sure text column exists and has no NaNs
    if "clean_text" not in df.columns:
        raise ValueError("clean_text column not found. Run nlp_preprocess.py first.")

    # Replace NaN with empty strings
    df["clean_text"] = df["clean_text"].fillna("").astype(str)

    print("🔍 Extracting themes using TF-IDF...")

    results = []

    for bank in df["bank"].dropna().unique():
        subset = df[df["bank"] == bank].copy()

        # Drop rows where clean_text is empty
        subset = subset[subset["clean_text"].str.strip() != ""]

        if subset.empty:
            continue

        vectorizer = TfidfVectorizer(
            max_features=1000,
            ngram_range=(1, 2)
        )
        tfidf_matrix = vectorizer.fit_transform(subset["clean_text"])

        scores = tfidf_matrix.sum(axis=0).A1
        terms = vectorizer.get_feature_names_out()

        top_indices = scores.argsort()[::-1][:top_n]
        top_terms = [(terms[i], scores[i]) for i in top_indices]

        for term, score in top_terms:
            results.append([bank, term, float(score)])

    theme_df = pd.DataFrame(results, columns=["bank", "term", "score"])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    theme_df.to_csv(output_path, index=False)

    print(f"✔ Theme extraction complete! Saved to: {output_path}")

if __name__ == "__main__":
    extract_themes()


