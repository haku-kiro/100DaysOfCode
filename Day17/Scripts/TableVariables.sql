-- Working with table variables

DECLARE @ThisIsATableVar TABLE
(
	Name varchar(100)
)
--Can then use the table var, by inserting data - filtering it - changing it - etc
INSERT INTO @ThisIsATableVar
SELECT name
FROM sys.databases

SELECT *
FROM @ThisIsATableVar -- Use a better example

DELETE FROM @ThisIsATableVar
WHERE Name = 'CRM' --DANGER

SELECT *
FROM @ThisIsATableVar