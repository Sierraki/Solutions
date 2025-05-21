SELECT  name   AS NAME
       ,blance AS BALANCE
FROM
(
	SELECT  u.account
	       ,u.name
	       ,round(SUM(amount),0) AS blance
	FROM Transactions t, users u
	WHERE u.account = t.account
	GROUP BY  account
) AS t1
WHERE blance > 10000