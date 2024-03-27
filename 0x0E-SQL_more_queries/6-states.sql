-- database hbtn_0d_usa
-- creates the table states in this db
-- If the table/db already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY, name VARCHAR(256) NOT NULL);
