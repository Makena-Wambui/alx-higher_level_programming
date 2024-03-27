-- Displays the top 3 of cities temperature during July and August ordered by temperature (descending)
-- Use SELECT clause, plus ORDER BY, and GROUP BY, and WHERE to specify a condition (the months we are interested in)
-- GROUP By is used to organize data based on common values in specified columns
-- LIMIT ensures the result set has exactly three rows
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
