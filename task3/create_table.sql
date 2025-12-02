CREATE TABLE reviews (
    review_id TEXT PRIMARY KEY,
    bank TEXT,
    app_name TEXT,
    score INTEGER,
    content TEXT,
    at TIMESTAMP,
    source TEXT
);
