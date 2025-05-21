WITH a1 AS
(
	SELECT  p1.product_id product1_id
	       ,p2.product_id product2_id
	       ,COUNT(*) cnt
	FROM productpurchases p1
	CROSS JOIN test.productpurchases p2
	ON p1.user_id = p2.user_id
	WHERE p1.product_id < p2.product_id
	GROUP BY  p1.product_id
	         ,p2.product_id
	ORDER BY  p1.product_id
)
SELECT  product1_id
       ,product2_id
       ,p1.category product1_category
       ,p2.category product2_category
       ,cnt customer_count
FROM a1
LEFT JOIN productinfo p1
ON product1_id = p1.product_id
LEFT JOIN productinfo p2
ON product2_id = p2.product_id
WHERE cnt >= 3
ORDER BY customer_count desc, product1_id, product2_id