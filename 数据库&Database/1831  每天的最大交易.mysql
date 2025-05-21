SELECT  transaction_id
FROM
(
	SELECT  transaction_id
	       ,rank() OVER (PARTITION BY day ORDER BY  amount DESC) A
	FROM Transactions
)t1
WHERE A = 1
ORDER BY transaction_id