WITH a1 AS
(
	SELECT  task_id tid
	       ,employee_id id
	       ,start_time s
	       ,end_time e
	FROM tasks
) , a2 as(
SELECT  *
       ,lead(s)over(PARTITION BY id ORDER BY  s) s1
       ,lead(e)over(PARTITION BY id ORDER BY s) e1
FROM a1) , a3 AS
(
	SELECT  *
	       ,CASE WHEN s1 BETWEEN s AND e and( e1 >= e )then timestampdiff(minute,s1,e)
	             WHEN s1 BETWEEN s AND e and( e1 < e )then timestampdiff(minute,s1,e1)  ELSE 0 END AS overlap
	       ,timestampdiff(minute,s,e) odiff
	FROM a2
) , a4 AS
(
	SELECT  id employee_id
	       ,FLOOR((SUM(odiff)-SUM(overlap))/60)total_task_hours
	FROM a3
	GROUP BY  id
)/*total*/ , a5 AS (
SELECT  employee_id id
       ,start_time st
       ,end_time en
FROM tasks) , a6 AS
(
	SELECT  id
	       ,st
	       ,1 AS A
	FROM a5
	UNION ALL
	SELECT  id
	       ,en
	       ,-1
	FROM a5
) , a7 AS
(
	SELECT  *
	       ,SUM(A)over(PARTITION BY id ORDER BY  st)num
	FROM a6
) , a8 AS
(
	SELECT  id employee_id
	       ,MAX(num) max_concurrent_tasks
	FROM a7
	GROUP BY  id
)
SELECT  *
FROM a4
LEFT JOIN a8 using
(employee_id
)
ORDER BY employee_id