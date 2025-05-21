WITH a1 AS
(
	SELECT  product_id
	       ,category
	       ,price
	       ,ifnull(discount,0) discount
	FROM products
	LEFT JOIN discounts using
	(category
	)
)
SELECT  product_id
       ,price*(100-discount)/100 final_price
       ,category
FROM a1
ORDER BY product_id