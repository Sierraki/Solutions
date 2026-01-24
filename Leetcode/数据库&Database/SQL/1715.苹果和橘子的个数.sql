WITH t1 as
(
	SELECT  b.*
	       ,c.apple_count  AS chest_apple_count
	       ,c.orange_count AS chest_orange_count
	FROM Boxes b
	JOIN Chests c
	ON b.chest_id = c.chest_id
) , apples as(
SELECT  SUM(apple_count ) AS apple_count
FROM
(
	SELECT  SUM(apple_count) AS apple_count
	FROM Boxes
	UNION ALL
	SELECT  SUM(chest_apple_count) AS apple_count
	FROM t1
) tmp1 ) , oranges as(
SELECT  SUM(orange_count ) AS orange_count
FROM
(
	SELECT  SUM(orange_count) AS orange_count
	FROM Boxes
	UNION ALL
	SELECT  SUM(chest_orange_count) AS orange_count
	FROM t1
) tmp2 )
SELECT  apple_count
       ,orange_count
FROM apples , oranges