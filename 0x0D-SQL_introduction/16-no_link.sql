-- Lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- Results should display the score and the name (in this order)
-- Don’t list rows without a name value
-- Records should be listed by descending score
-- Use SELECT Clause, and IS NOT NULL option
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
