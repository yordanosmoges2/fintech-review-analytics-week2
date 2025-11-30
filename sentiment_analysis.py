import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load cleaned data
df = pd.read_csv("data/clean_reviews.csv")

analyzer = SentimentIntensityAnalyzer()

# Compute sentiment score
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))['compound']
    if score > 0.05:
        return "positive"
    elif score < -0.05:
        return "negative"
    else:
        return "neutral"

def get_score(text):
    return analyzer.polarity_scores(str(text))['compound']

df["sentiment_score"] = df["content"].apply(get_score)
df["sentiment_label"] = df["content"].apply(get_sentiment)

# Save output
df.to_csv("data/sentiment_reviews.csv", index=False)

print("Sentiment analysis complete! Saved as data/sentiment_reviews.csv")
