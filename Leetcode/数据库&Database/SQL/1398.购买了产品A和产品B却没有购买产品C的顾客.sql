WITH a1 AS
(
	SELECT  customer_id
	FROM orders
	WHERE product_name = 'A' 
), b1 AS
(
	SELECT  customer_id
	FROM orders
	WHERE product_name = 'B' 
), c1 AS
(
	SELECT  customer_id
	FROM orders
	WHERE product_name = 'C' 
)
SELECT  distinct a1.customer_id
       ,customer_name
FROM a1
LEFT JOIN b1
ON a1.customer_id = b1.customer_id
LEFT JOIN c1
ON a1.customer_id = c1.customer_id
LEFT JOIN customers c
ON c.customer_id = a1.customer_id
WHERE a1.customer_id is not null
AND b1.customer_id is not null
AND c1.customer_id is null