SELECT  customer_id
FROM
(
	SELECT  customer_id
	       ,COUNT(distinct product_key) AS cc
	FROM customer
	GROUP BY  customer_id
)as t1
WHERE cc = (
SELECT  COUNT(product_key)
FROM Product )