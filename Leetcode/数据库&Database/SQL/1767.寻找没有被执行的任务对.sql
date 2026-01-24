WITH RECURSIVE numbers AS
(
	SELECT  1 AS num
	UNION ALL
	SELECT  num + 1
	FROM numbers
	WHERE num < 20 
), a1 AS
(
	SELECT  task_id
	       ,num
	FROM Tasks
	CROSS JOIN numbers
	WHERE num <= subtasks_count
	ORDER BY task_id
)
SELECT  task_id
       ,num subtask_id
FROM a1
WHERE (task_id, num ) NOT IN ( SELECT task_id, subtask_id FROM Executed )