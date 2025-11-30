import pandas as pd

df = pd.read_csv("data/raw_reviews.csv")

print("Number of columns:", len(df.columns))
print("Column names:")
print(df.columns.tolist())




