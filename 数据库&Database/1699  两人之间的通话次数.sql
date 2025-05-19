WITH a1 AS
(
	SELECT  from_id person1
	       ,to_id person2
	       ,duration
	FROM calls
	WHERE from_id < to_id 
), a2 AS
(
	SELECT  to_id person1
	       ,from_id person2
	       ,duration
	FROM calls
	WHERE to_id < from_id 
), a3 AS
(
	SELECT  *
	FROM a1
	UNION ALL
	SELECT  *
	FROM a2
)
SELECT  distinct person1
       ,person2
       ,duration call_count
       ,total_duration
FROM
(
	SELECT  person1
	       ,person2
	       ,COUNT(*) OVER (PARTITION BY person1,person2) duration
	       ,SUM(duration) OVER (PARTITION BY person1,person2) total_duration
	FROM a3
)t1