from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.cbe.mobilebanking",
    "BOA": "com.boa.mobilebanking",
    "Dashen": "com.dashen.bank"
}

all_reviews = []

# Try 10 regions where Ethiopian users commonly download apps
countries = ["et", "it", "us", "gb", "ng", "ke", "za", "ae", "sa", "in"]

for bank, app_id in apps.items():
    print(f"\nScraping {bank} ({app_id})...")

    bank_reviews = []

    for country in countries:
        print(f"  Trying country store: {country}...")

        try:
            rvs, _ = reviews(
                app_id,
                lang="en",
                country=country,
                sort=Sort.NEWEST,
                count=500
            )

            if len(rvs) > 0:
                print(f"    ✓ Got {len(rvs)} reviews from {country}")
                bank_reviews = rvs
                break
            else:
                print(f"    ⚠ No reviews found for {country}")

        except Exception as e:
            print(f"    ❌ Error for {country}: {e}")

    for r in bank_reviews:
        all_reviews.append({
            "review": r.get("content", ""),
            "rating": r.get("score", None),
            "date": r.get("at", None),
            "bank": bank,
            "source": "Google Play"
        })

print("\nFINISHED SCRAPING!")
print("Total reviews scraped:", len(all_reviews))

df = pd.DataFrame(all_reviews)
df.to_csv("raw_reviews.csv", index=False)

print("\nSaved to raw_reviews.csv")

