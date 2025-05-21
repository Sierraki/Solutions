WITH a1 AS
(
	SELECT  invoice_id
	       ,pu.product_id
	       ,quantity
	       ,quantity*price summ
	FROM purchases pu
	LEFT JOIN products pr
	ON pr.product_id = pu.product_id
), a2 AS
(
	SELECT  *
	       ,SUM(summ) total
	FROM a1
	GROUP BY  invoice_id
	ORDER BY  total desc
	         ,invoice_id
	LIMIT 1
)
SELECT  product_id
       ,quantity
       ,summ price
FROM a1
WHERE invoice_id = (
SELECT  invoice_id
FROM a2 )