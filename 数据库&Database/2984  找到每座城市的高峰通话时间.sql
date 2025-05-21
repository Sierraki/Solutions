WITH a1 AS
(
	SELECT  hour(call_time) t1
	       ,city
	FROM calls
) , a2 AS
(
	SELECT  *
	       ,COUNT(*) OVER (PARTITION BY city,t1) c
	FROM a1
) , a3 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY city ORDER BY  c DESC) r
	FROM a2
)
SELECT  distinct city
       ,t1 peak_calling_hour
       ,c number_of_calls
FROM a3
WHERE r = 1
ORDER BY peak_calling_hour desc, city DESC 