WITH a1 AS
(
	SELECT  user_id
	       ,steps_count c1
	       ,steps_date d1
	       ,lead(steps_count)over(PARTITION BY user_id ORDER BY  steps_date)c2
	       ,lead(steps_date)over(PARTITION BY user_id ORDER BY steps_date)d2
	       ,lead(steps_count,2)over(PARTITION BY user_id ORDER BY steps_date)c3
	       ,lead(steps_date,2)over(PARTITION BY user_id ORDER BY steps_date)d3
	FROM steps
)
SELECT  user_id
       ,d3 steps_date
       ,round((c1+c2+c3)/3,2) rolling_average
FROM a1
WHERE DATEDIFF(d2, d1) = 1
AND DATEDIFF(d3, d2) = 1
ORDER BY user_id, steps_date