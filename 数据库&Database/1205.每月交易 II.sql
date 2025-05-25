WITH CTE AS
(
	SELECT  *
	FROM Transactions
	UNION ALL
	SELECT  t.id
	       ,country
	       ,'chargeback' state
	       ,amount
	       ,c.trans_date
	FROM Chargebacks c
	LEFT JOIN Transactions t
	ON c.trans_id = t.id
)
SELECT  DATE_FORMAT(trans_date,'%Y-%m')        AS month
       ,country
       ,SUM(IF(state = 'approved',1,0))        AS approved_count
       ,SUM(IF(state = 'approved',amount,0))   AS approved_amount
       ,SUM(IF(state = 'chargeback',1,0))      AS chargeback_count
       ,SUM(IF(state = 'chargeback',amount,0)) AS chargeback_amount
FROM CTE
GROUP BY  1
         ,2
HAVING approved_count or chargeback_count