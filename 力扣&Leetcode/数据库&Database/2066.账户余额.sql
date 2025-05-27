WITH a1 AS
(
	SELECT  account_id
	       ,day
	       ,if(type = 'Withdraw',-1*amount,amount) amount
	FROM Transactions
	ORDER BY account_id, day
)
SELECT  account_id
       ,day
       ,SUM(amount) OVER (PARTITION BY account_id ORDER BY  day) balance
FROM a1