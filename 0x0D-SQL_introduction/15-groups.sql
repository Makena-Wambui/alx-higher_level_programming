-- Lists the number of records with the same score
-- Use SELECT clause, plus ORDER BY, and GROUP BY
-- GROUP By is used to organize data based on common values in specified columns
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
