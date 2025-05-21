SELECT  round(SUM(tiv_2016) ,2)as tiv_2016
FROM
(
	SELECT  t1.pid
	FROM
	(
		SELECT  pid
		FROM Insurance
		WHERE pid NOT IN ( SELECT pid FROM insurance GROUP BY tiv_2015 HAVING COUNT(tiv_2016) = 1)
	)t1, (
	SELECT  i.pid
	FROM insurance i
	GROUP BY  lat
	         ,lon
	HAVING COUNT(pid) = 1) t2
	WHERE t1.pid = t2.pid
)t3
JOIN insurance i
ON i.pid = t3.pid