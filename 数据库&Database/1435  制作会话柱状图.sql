WITH a1 AS
(
	SELECT  CASE WHEN A >= 0 AND A < 5 THEN '[0-5>'
	             WHEN A >= 5 AND A < 10 THEN '[5-10>'
	             WHEN A >= 10 AND A < 15 THEN '[10-15>'  ELSE '15 or more' END AS bin
	       ,COUNT(*) total
	FROM
	(
		SELECT  *
		       ,duration/60 A
		FROM sessions
	)t1
	GROUP BY  bin
), a2 AS
(
	SELECT  '[0-5>' bin
	UNION
	SELECT  '[5-10>' bin
	UNION
	SELECT  '[10-15>' bin
	UNION
	SELECT  '15 or more' bin
)
SELECT  a2.bin
       ,ifnull(total,0) total
FROM a2
LEFT JOIN a1
ON a2.bin = a1. bin