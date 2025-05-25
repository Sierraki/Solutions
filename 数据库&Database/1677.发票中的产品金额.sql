SELECT  p.NAME
       ,ifnull( SUM( i.rest ),0 )     AS rest
       ,ifnull( SUM( i.paid ),0 )     AS paid
       ,ifnull( SUM( i.canceled ),0 ) AS canceled
       ,ifnull( SUM( i.refunded ),0 ) AS refunded
FROM Product AS p
LEFT JOIN Invoice AS i
ON p.product_id = i.product_id
GROUP BY  p.product_id
ORDER BY  p.NAME