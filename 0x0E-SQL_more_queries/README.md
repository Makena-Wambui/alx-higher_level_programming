Creating a user account using the Create User Statement.

Grant privilleges to a particular user

Show privilleges for each user

Revoke privilleges for each user

MySql Constraints: Limit how we insert data into a table

Types of Constraints
--------------------
Primary Key
Foreign Key
ENUM
SET
NOT NULL
UNIQUE

AUTO INCREMENT FEATURE:
Allows you to automatically generate unque values in a column every time a new row is inserted into a table.
Useful for creating primary key fields that need to be created automatically every time a new record is inserted.
Use AUTO_INCREMENT Keyword.

SUBQUERIES
--------------
A query within another query.
The outer query is the main query.
The inner query is the subquery.
Can be used in WHERE, FROM and HAVING Clauses
Can be used with SELECT, INSERT INTO, UPDATE and DELETE FROM statements.

Enclosed in ()
Cannot have ORDER BY statement, but can use GROUP BY

INNER JOIN:
All shared data between two relations.
All records existing in both relations that match the ON condition

FULL JOIN
Fetch all data from left
Fetch all data from right.
If record exists on right but not on left, then Null and viceversa

FULL JOIN WITHOUT INTERSECTION
ALL in both
Excludes those in common.

LEFT JOIN
ALL data from left
Only matching from right.
Non matching in right = NULL
