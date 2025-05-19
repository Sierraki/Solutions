WITH a1 AS
(
	SELECT  *
	       ,rank() OVER (PARTITION BY user_id ORDER BY  Transaction_date) r
	       ,lag(spend)over (PARTITION BY user_id ORDER BY Transaction_date) d1
	FROM Transactions
), a2 AS
(
	SELECT  *
	       ,lag(d1)over (PARTITION BY user_id ORDER BY  Transaction_date) d2
	FROM a1
)
SELECT  user_id
       ,spend third_transaction_spend
       ,transaction_date third_transaction_date
FROM a2
WHERE spend > d1
AND spend > d2
AND r = 3