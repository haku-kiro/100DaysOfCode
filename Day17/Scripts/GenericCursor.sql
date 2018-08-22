-- Writing a generic cursor


--Define some vars 
DECLARE @DBName varchar(250)

-- STEP 1: Declare cursor
DECLARE ACursor CURSOR FOR
--Data Query
SELECT name
FROM sys.databases

-- STEP 2: Open the cursor
OPEN ACursor

-- STEP 3: insert a row into the outer var to work with (Can return more than one col; comma seperate the vars)
-- and work with that data
FETCH NEXT FROM ACursor INTO @DBName

WHILE @@FETCH_STATUS = 0 -- A fetch status of zero means that it was successful
--Perfom action
BEGIN
	PRINT @DBName -- Just printing the name, but you can do what ever you'd like here
	--Make sure to iterate (Just like a while loop)
	FETCH NEXT FROM ACursor INTO @DBName -- by iterate, you just need to get the next row from the cursor into the variables
END

-- STEP 4: Close your cursor
CLOSE ACursor

-- STEP 5: Deallocate your cursor
DEALLOCATE ACursor