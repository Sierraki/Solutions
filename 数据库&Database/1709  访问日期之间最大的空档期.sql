WITH a1 AS
(
	SELECT  user_id
	       ,visit_date
	       ,lead(visit_date) OVER (PARTITION BY user_id ORDER BY  visit_date ASC) A
	FROM UserVisits
), a2 AS
(
	SELECT  user_id
	       ,visit_date A1
	       ,ifnull(A,'2021-1-1') A2
	FROM a1
)
SELECT  distinct user_id
       ,MAX(DATEDIFF(A2,A1)) OVER ( PARTITION BY user_id) biggest_window
FROM a2
ORDER BY user_id