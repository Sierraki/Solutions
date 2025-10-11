WITH t1 AS
(
	SELECT  distinct seller_id
	FROM orders
	WHERE year(sale_date) = 2020
), t2 AS
(
	SELECT  s.seller_name
	       ,t1.seller_id
	FROM seller s
	LEFT JOIN t1
	ON t1.seller_id = s.seller_id
)
SELECT  seller_name
FROM t2
WHERE seller_id is null
ORDER BY seller_name 