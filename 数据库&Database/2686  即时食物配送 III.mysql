WITH a1 AS
(
	SELECT  delivery_id
	       ,order_date
	       ,CASE WHEN order_date = customer_pref_delivery_date THEN 'A'  ELSE 'B' END AS sta
	FROM delivery
), a2 AS
(
	SELECT  distinct order_date
	       ,sta
	       ,COUNT(*) OVER (PARTITION BY order_date,sta) countt
	FROM a1
	WHERE sta = 'A'
), a3 AS
(
	SELECT  distinct order_date
	       ,sta
	       ,COUNT(*) OVER (PARTITION BY order_date,sta) countt
	FROM a1
	WHERE sta = 'B' 
), a4 AS
(
	SELECT  distinct d.order_date
	       ,ifnull(a2.countt,0)A
	       ,ifnull(a3.countt,0) B
	FROM Delivery d
	LEFT JOIN a2
	ON d.order_date = a2.order_date
	LEFT JOIN a3
	ON d.order_date = a3.order_date
)
SELECT  order_date
       ,round(A*100/(A+B),2) immediate_percentage
FROM a4
ORDER BY order_date