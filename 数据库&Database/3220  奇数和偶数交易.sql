SELECT  t.transaction_date
       ,t1.odd_sum
       ,SUM(if(amount%2 = 1,0,amount))as even_sum
FROM transactions t,
(
	SELECT  transaction_date
	       ,SUM(if(amount%2 = 0,0,amount))as odd_sum
	FROM transactions
	GROUP BY  transaction_date
)as t1
WHERE t1.transaction_date = t.transaction_date
GROUP BY  transaction_date
ORDER BY  transaction_date asc