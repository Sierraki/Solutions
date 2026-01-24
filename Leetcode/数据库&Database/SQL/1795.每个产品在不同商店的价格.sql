select*
FROM
(
	SELECT  product_id
	       ,'store1'as store
	       ,store1 AS price
	FROM products
	UNION
	SELECT  product_id
	       ,'store2'as store
	       ,store2 AS price
	FROM products
	UNION
	SELECT  product_id
	       ,'store3'as store
	       ,store3 AS price
	FROM products
)as t1
WHERE price is not null