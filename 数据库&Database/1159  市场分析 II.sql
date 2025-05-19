WITH a1 AS
(
	SELECT  seller_id
	       ,item_id
	       ,ROW_NUMBER() OVER (PARTITION BY seller_id ORDER BY  order_date ASC) A
	FROM orders
), a2 AS
(
	SELECT  a1.seller_id
	       ,item_brand
	FROM a1, Items
	WHERE Items.item_id = a1.item_id
	AND A = 2
)
SELECT  u.user_id seller_id
       ,if(favorite_brand = item_brand,'yes','no') 2nd_item_fav_brand
FROM users u
LEFT JOIN a2
ON u.user_id = a2.seller_id