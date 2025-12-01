import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import os

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = word_tokenize(text)

    stop_words = set(stopwords.words("english"))
    tokens = [t for t in tokens if t not in stop_words]

    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return " ".join(tokens)

def preprocess_nlp(input_path="data/clean_reviews.csv",
                    output_path="data/nlp_reviews.csv"):

    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("wordnet")

    df = pd.read_csv(input_path)

    print("📝 Cleaning text for NLP...")
    df["clean_text"] = df["content"].astype(str).apply(clean_text)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"✔ NLP preprocessing complete! Saved to: {output_path}")

if __name__ == "__main__":
    preprocess_nlp()
