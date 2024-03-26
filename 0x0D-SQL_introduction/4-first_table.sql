-- This script demonstrates how to create a table in a db.
-- We use the CREATE TABLE Query and IF NOT EXISTS option to ensure script does not fail.
-- CREATE TABLE table_name (column1_name datatype(size), column2_name datatype(size));
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
