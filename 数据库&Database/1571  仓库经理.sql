WITH a1 as
(
	SELECT  product_id
	       ,Width*Length*Height AA
	FROM products
)
SELECT  name warehouse_name
       ,SUM(units*AA) volume
FROM Warehouse w
LEFT JOIN a1
ON w.product_id = a1.product_id
GROUP BY  name