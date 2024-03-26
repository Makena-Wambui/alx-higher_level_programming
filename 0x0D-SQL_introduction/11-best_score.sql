-- List specific records
-- Results should display both the score and the name (in this order)
-- Record ordered by score, top score first.
-- Condition: score >= 10
-- Use the SELECT clause plus ORDER BY plus WHERE
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
