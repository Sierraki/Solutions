SELECT  MIN(round(sqrt(pow(x-x1,2)+pow(y-y1,2)),2)) AS shortest
FROM
(
	SELECT  p1.x
	       ,p1.y
	       ,p2.x x1
	       ,p2.y y1
	FROM point2d p1, point2d p2
)t1
WHERE (x, y) <> (x1, y1) 