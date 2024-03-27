
-- Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- Use SELECT clause, plus ORDER BY, and GROUP BY
-- GROUP By is used to organize data based on common values in specified columns
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
