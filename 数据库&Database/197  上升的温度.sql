SELECT  w.id
FROM weather w
INNER JOIN
(
	SELECT  DATE_ADD(a.recordDate,INTERVAL 1 DAY) AS recorddate
	       ,a.temperature
	FROM weather a
)as a
ON w.recorddate = a.recorddate
WHERE a.temperature < w.temperature 