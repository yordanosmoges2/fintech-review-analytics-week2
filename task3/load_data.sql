\copy reviews(review_id, bank, app_name, score, content, at, source)
FROM 'data/clean_reviews.csv'
WITH (
    FORMAT csv,
    HEADER true,
    ENCODING 'UTF8',
    QUOTE '"',
    ESCAPE '"'
);
