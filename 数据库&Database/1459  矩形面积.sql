WITH a1 AS
(
	SELECT  p.id
	       ,t1.id id1
	FROM points p
	CROSS JOIN
	(
		SELECT  id
		FROM points
	)t1
	WHERE p.id <> t1.id 
), a2 AS
(
	SELECT  a1.id
	       ,id1
	       ,p.x_value x
	       ,p.y_value y
	       ,p1.x_value x1
	       ,p1.y_value y1
	FROM a1
	LEFT JOIN Points p
	ON p.id = a1.id
	LEFT JOIN Points p1
	ON id1 = p1.id
), a3 AS
(
	SELECT  *
	       ,abs(x-x1)*abs(y-y1) AA
	FROM a2
)
SELECT  id P1
       ,id1 P2
       ,AA AREA
FROM a3
WHERE AA <> 0
AND id < id1
ORDER BY AA desc, id asc, id1 asc