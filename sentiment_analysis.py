import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
import matplotlib.pyplot as plt
import seaborn as sns

def run_sentiment(input_path="data/nlp_reviews.csv",
                  output_path="data/sentiment_reviews.csv"):

    df = pd.read_csv(input_path)

    analyzer = SentimentIntensityAnalyzer()

    print("🔎 Running sentiment analysis...")

    # Compute sentiment score
    df["sentiment_score"] = df["clean_text"].apply(
        lambda x: analyzer.polarity_scores(str(x))["compound"]
    )

    # Label sentiment
    df["sentiment_label"] = df["sentiment_score"].apply(
        lambda s: "positive" if s > 0.05 else ("negative" if s < -0.05 else "neutral")
    )

    # Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✔ Sentiment analysis complete! Saved to: {output_path}")

    # -------------------------------------------------------
    # 📊 VISUALIZATION SECTION (inside the function!)
    # -------------------------------------------------------

    print("📊 Creating visualizations...")

    # Ensure folder exists
    os.makedirs("data/plots", exist_ok=True)

    # 1. Sentiment Category Count Plot
    plt.figure(figsize=(7,5))
    sns.countplot(x="sentiment_label", data=df, palette="coolwarm")
    plt.title("Sentiment Category Counts")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.savefig("data/plots/sentiment_category_counts.png")
    plt.close()

    # 2. Sentiment Score Distribution
    plt.figure(figsize=(7,5))
    sns.histplot(df["sentiment_score"], bins=20, kde=True)
    plt.title("Sentiment Score Distribution")
    plt.xlabel("Sentiment Score")
    plt.ylabel("Frequency")
    plt.savefig("data/plots/sentiment_score_distribution.png")
    plt.close()

    print("✔ All visualizations saved in data/plots/")

if __name__ == "__main__":
    run_sentiment()



