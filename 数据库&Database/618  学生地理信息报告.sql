WITH m as
(
	SELECT  name                                 AS America
	       ,ROW_NUMBER() over(order by name ASC) AS id
	FROM student
	WHERE continent = 'America' 
), o as(
SELECT  name                                  AS Europe
       ,ROW_NUMBER() OVER (order by name ASC) AS id
FROM student
WHERE continent = 'Europe' ), y as(
SELECT  name                                  AS Asia
       ,ROW_NUMBER() OVER (order by name ASC) AS id
FROM student
WHERE continent = 'Asia' )
SELECT  America
       ,Asia
       ,Europe
FROM m
LEFT JOIN y
ON m.id = y.id
LEFT JOIN o
ON m.id = o.id