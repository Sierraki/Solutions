WITH a1 AS
(
	SELECT  log_id
	       ,ROW_NUMBER() OVER (order by log_id) A
	       ,log_id-ROW_NUMBER() OVER (order by log_id) B
	FROM logs
)
SELECT  distinct *
FROM
(
	SELECT  MIN(log_id) OVER (PARTITION BY B) start_id
	       ,MAX(log_id) OVER (PARTITION BY B) end_id
	FROM a1
)t1