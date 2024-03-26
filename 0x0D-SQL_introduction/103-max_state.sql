-- Displays the max temperature of each state (ordered by State name).
-- Use SELECT clause, plus ORDER BY, and GROUP BY
-- GROUP By is used to organize data based on common values in specified columns
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
