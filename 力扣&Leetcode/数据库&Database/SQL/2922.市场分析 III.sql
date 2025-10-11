WITH t AS
(
	SELECT  seller_id
	       ,COUNT(distinct item_id) num_items
	FROM items i
	JOIN orders o USING
	(item_id
	)
	JOIN users u USING
	(seller_id
	)
	WHERE i.item_brand <> u.favorite_brand
	GROUP BY  seller_id
)
SELECT  *
FROM t
WHERE num_items = (
SELECT  MAX(num_items)
FROM t)