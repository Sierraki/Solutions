WITH a1 AS
(
	SELECT  date_format(order_date,'%Y-%m') month
	       ,customer_id
	       ,invoice
	       ,order_id
	FROM orders
	WHERE invoice > 20 
)
SELECT  month
       ,COUNT(*) order_count
       ,COUNT(distinct customer_id) customer_count
FROM a1
GROUP BY  month