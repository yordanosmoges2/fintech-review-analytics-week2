Fintech Review Analytics – Week 2

Author: Yordanos Moges
Course: 10 Academy – Week 2 Challenge
Project: App Review Scraping, NLP Preprocessing, Sentiment Analysis & Thematic Extraction

📌 Project Overview

This project builds a full end-to-end NLP pipeline for analyzing customer reviews of Ethiopian fintech applications. The workflow includes:

Scraping Play Store reviews

Preprocessing raw text (cleaning, column alignment, date normalization)

Sentiment analysis using VADER

Theme extraction using TF-IDF + clustering

Structured outputs exported for analysis

The goal is to transform raw, unstructured customer feedback into actionable insights for improving fintech apps.

📂 Repository Structure
fintech-review-analytics-week2/
│
├── data/
│   ├── raw_reviews.csv
│   ├── clean_reviews.csv
│   ├── sentiment_reviews.csv
│   └── themed_reviews.csv
│
├── scrape_reviews.py
├── preprocess.py
├── sentiment_analysis.py
├── theme_extraction.py
│
├── requirements.txt
└── README.md

⚙️ Setup & Installation
1. Clone the repository
git clone https://github.com/yordanosmoges2/fintech-review-analytics-week2.git
cd fintech-review-analytics-week2

2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

🧪 How to Run the Pipeline (Step-by-Step)
✔ Step 1 — Scrape Play Store Reviews
python scrape_reviews.py


Output:

Saves data/raw_reviews.csv

At least 400 reviews per bank are collected

✔ Step 2 — Preprocess the Raw Data

This script:
✓ Removes missing reviews
✓ Normalizes dates
✓ Fixes inconsistent column names
✓ Prints review counts per bank
✓ Ensures data quality

Run:

python preprocess.py


Output:

data/clean_reviews.csv

✔ Step 3 — Sentiment Analysis (VADER)
python sentiment_analysis.py


The script:

Computes positive / neutral / negative sentiment

Adds compound scores

Generates sentiment distribution

Output:

data/sentiment_reviews.csv

✔ Step 4 — Theme Extraction (TF-IDF + Clustering)
python theme_extraction.py


The script:

Cleans and tokenizes text

Removes NaN values

Extracts top keywords per cluster

Groups similar customer issues

Output:

data/themed_reviews.csv

🧠 Pipeline Diagram
Scraping → Preprocessing → Sentiment Analysis → Theme Extraction → Outputs

📊 Outputs & Their Meaning
File	Description
raw_reviews.csv	Raw scraped data from Play Store
clean_reviews.csv	Cleaned dataset with aligned columns & normalized text
sentiment_reviews.csv	Sentiment scores (positive, neutral, negative, compound)
themed_reviews.csv	Assigned themes + extracted keywords per review
🧩 Assumptions

Each bank must have ≥400 reviews (validated in preprocessing).

Input file locations follow the data/ folder structure.

Scripts are run in sequence (scraping → preprocess → sentiment → themes).

VADER and TF-IDF are sufficient for baseline NLP; advanced models can be added later.

📈 Future Improvements

To reach a higher professional level (as recommended):

Add spaCy NLP preprocessing (tokenization, lemmatization)

Replace keyword-based themes with ML-based topic modeling (LDA, BERTopic)

Add unit tests for data validation

Integrate dashboards for insights visualization

✨ Acknowledgement

This project was completed as part of the 10 Academy Week 2 challenge, with guidance from the feedback provided by mentors and automated scoring.