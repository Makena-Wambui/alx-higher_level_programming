-- Creates the MySQL server user user_0d_2
-- creates the database hbtn_0d_2
-- if the db exists script shd not fail
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- If the user user_0d_2 already exists, your script should not fail
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
