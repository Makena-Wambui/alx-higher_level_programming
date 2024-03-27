-- creates the table unique_id
-- If the table already exists, your script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));
