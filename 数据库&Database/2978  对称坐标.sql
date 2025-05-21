WITH a1 AS
(
	SELECT  c1.x x1
	       ,c1.y y1
	       ,c2.x x2
	FROM Coordinates c1
	CROSS JOIN Coordinates c2
), a2 AS
(
	SELECT  x1
	       ,y1
	       ,x2
	       ,c.y y2
	FROM a1
	LEFT JOIN Coordinates c
	ON a1.x2 = c.x
), a3 AS
(
	SELECT  x1 X
	       ,y1 Y
	       ,COUNT(*)over (PARTITION BY x1) A
	FROM a2
	WHERE x1 = y2
	AND x2 = y1
	AND x1 = y1 
)
SELECT  distinct X
       ,Y
FROM a3
WHERE A > 6 
UNION ALL
SELECT  distinct x1 X
       ,y1 Y
FROM a2
WHERE x1 = y2
AND x2 = y1
AND x1 <= y1
AND x1 <> y1
ORDER BY X, Y