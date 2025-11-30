import pandas as pd

# Load sentiment data
df = pd.read_csv("data/sentiment_reviews.csv")

# Simple theme detection using keyword rules
def detect_theme(text):
    text = str(text).lower()

    if any(word in text for word in ["login", "password", "otp", "signin"]):
        return "Account Access Issues"

    if any(word in text for word in ["slow", "lag", "load", "loading", "delay"]):
        return "Performance Issues"

    if any(word in text for word in ["crash", "freeze", "error", "bug"]):
        return "App Reliability"

    if any(word in text for word in ["ui", "design", "interface", "layout"]):
        return "User Interface"

    if any(word in text for word in ["feature", "add", "improve", "request"]):
        return "Feature Requests"

    return "Other"

df["theme"] = df["content"].apply(detect_theme)

df.to_csv("data/themed_reviews.csv", index=False)

print("Theme extraction complete! Saved as data/themed_reviews.csv")
