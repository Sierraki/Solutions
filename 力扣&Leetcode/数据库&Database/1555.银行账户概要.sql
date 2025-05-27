WITH a1 AS
(
	SELECT  paid_by id
	       ,-1*amount amount
	FROM Transactions
	UNION ALL
	SELECT  paid_to id
	       ,amount
	FROM Transactions
), a2 AS
(
	SELECT  id
	       ,SUM(amount) amount
	FROM a1
	GROUP BY  id
), a3 AS
(
	SELECT  user_id
	       ,user_name
	       ,ifnull(amount,0)+credit credit
	FROM users u
	LEFT JOIN a2
	ON a2.id = u.user_id
)
SELECT  *
       ,CASE WHEN credit < 0 THEN 'Yes'  ELSE 'No' END AS credit_limit_breached
FROM a3