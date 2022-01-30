CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question VARCHAR(255),
    answer1 VARCHAR(255),
    answer2 VARCHAR(255),
    answer3 VARCHAR(255),
    answer4 VARCHAR(255),
    correct TINYINT
);