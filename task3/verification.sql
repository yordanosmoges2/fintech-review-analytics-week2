-- Count total reviews
SELECT COUNT(*) FROM reviews;

-- Count reviews per bank
SELECT bank, COUNT(*) FROM reviews GROUP BY bank ORDER BY COUNT(*) DESC;

-- Rating distribution
SELECT score, COUNT(*) FROM reviews GROUP BY score ORDER BY score;

-- Sample rows
SELECT * FROM reviews LIMIT 5;
