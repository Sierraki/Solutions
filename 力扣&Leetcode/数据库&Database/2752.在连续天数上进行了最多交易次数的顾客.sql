WITH a1 AS
(
	SELECT  customer_id
	       ,to_days(transaction_date)d1
	       ,ROW_NUMBER()over(PARTITION BY customer_id ORDER BY  to_days(transaction_date)) num
	FROM transactions
) , a2 as(
SELECT  *
       ,d1-num
       ,COUNT(*)over(PARTITION BY customer_id,d1-num) A
FROM a1) , a3 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(PARTITION BY customer_id,d1-num) r
	FROM a2
)/**/
SELECT  customer_id
FROM a3
WHERE A = (
SELECT  MAX(A)
FROM a3 ) AND r = 1
ORDER BY customer_id