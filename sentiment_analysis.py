import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def run_sentiment(input_path="data/nlp_reviews.csv",
                  output_path="data/sentiment_reviews.csv"):

    df = pd.read_csv(input_path)

    analyzer = SentimentIntensityAnalyzer()

    print("🔎 Running sentiment analysis...")

    df["sentiment_score"] = df["clean_text"].apply(
        lambda x: analyzer.polarity_scores(str(x))["compound"]
    )

    df["sentiment_label"] = df["sentiment_score"].apply(
        lambda s: "positive" if s > 0.05 else ("negative" if s < -0.05 else "neutral")
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✔ Sentiment analysis complete! Saved to: {output_path}")

if __name__ == "__main__":
    run_sentiment()

