WITH a1 AS
(
	SELECT  user_id
	       ,time_stamp B
	       ,lead(time_stamp) OVER (PARTITION BY user_id ORDER BY  time_stamp) A
	FROM Confirmations
), a2 AS
(
	SELECT  *
	       ,timestampdiff(second,B,A) d
	FROM a1
	WHERE A is not null
)
SELECT  distinct user_id
FROM a2
WHERE d-24*60*60 <= 0