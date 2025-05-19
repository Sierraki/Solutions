WITH a1 AS
(
	SELECT  server_id id
	       ,status_time t1
	       ,session_status s1
	FROM servers
	ORDER BY server_id, status_time
) , a2 AS
(
	SELECT  *
	       ,lead(s1)over(PARTITION BY id ORDER BY  t1)s2
	       ,lag(s1)over(PARTITION BY id ORDER BY t1) s3
	FROM a1
) , a3 AS
(
	SELECT  id
	       ,t1
	       ,s1
	FROM a2
	WHERE (s1 = 'start' AND s3 is NULL) or (s1 = 'start' AND s2 = 'stop' AND s3 = 'stop') or (s1 = 'start' AND s2 = 'start' AND s3 = 'stop') or (s1 = 'stop' AND s3 = 'start') or (s1 = 'stop' AND s2 is NULL AND s3 = 'start') 
) , a4 AS
(
	SELECT  *
	       ,lead(t1)over(PARTITION BY id ORDER BY  t1) t2
	FROM a3
)
SELECT  FLOOR(SUM(timestampdiff(second,t1,t2))/60/60/24)total_uptime_days
FROM a4
WHERE s1 = 'start' 