CREATE TABLE IF NOT EXISTS accounts (
    id INT NOT NULL,
    username VARCHAR(50),
    password VARCHAR(50),
    age INT,
    gender VARCHAR(25),
    PRIMARY KEY(id)
)