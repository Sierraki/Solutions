WITH a1 AS
(
	SELECT  product_id
	       ,year(purchase_date) d
	FROM orders
	GROUP BY  product_id
	         ,d
	HAVING COUNT(*) >= 3
), a2 AS
(
	SELECT  *
	       ,d-lag(d) OVER (PARTITION BY product_id ORDER BY  d ) diff
	FROM a1
)
SELECT  distinct product_id
FROM a2
WHERE diff = 1