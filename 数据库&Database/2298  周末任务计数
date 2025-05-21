WITH a1 AS
(
	SELECT  *
	       ,CASE WHEN date_format(submit_date,'%w') = 0 or date_format(submit_date,'%w') = 6 THEN 1  ELSE 0 END AS d
	FROM tasks
), a2 AS
(
	SELECT  COUNT(*)working_cnt
	FROM a1
	WHERE d = 0
	GROUP BY  d
), a3 AS
(
	SELECT  COUNT(*)weekend_cnt
	FROM a1
	WHERE d = 1
	GROUP BY  d
)
SELECT  *
FROM a2, a3