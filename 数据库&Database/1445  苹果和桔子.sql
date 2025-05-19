WITH a1 AS
(
	SELECT  *
	FROM sales
	WHERE fruit = 'apples' 
), a2 AS
(
	SELECT  *
	FROM sales
	WHERE fruit = 'oranges' 
)
SELECT  a1.sale_date
       ,a1.sold_num-a2.sold_num diff
FROM a1
LEFT JOIN a2
ON a1.sale_date = a2.sale_date
ORDER BY a1.sale_date