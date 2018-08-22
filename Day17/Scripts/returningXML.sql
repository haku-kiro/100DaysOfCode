-- Returning data in xml format (Write a c# app to parse this - or don't that's cool)
-- Note, do some trimming

SELECT TOP 100 *
FROM dbo.Opportunity FOR XML RAW -- Basic xml format

--Click the result to return the xml data, right click> save as> to save file

SELECT TOP 100 *
FROM dbo.Opportunity FOR XML AUTO -- Root node with the table name?

-- I like this one the most, groups the rows in the path specified node 
--(This case, each row is a C4LOppo)
SELECT TOP 100 *
FROM dbo.Opportunity FOR XML PATH ('C4LOppo'), ROOT('CustomRootNode')
