SELECT  p.product_id
       ,ifnull(ROUND(SUM(p.price*ifnull(u.units,0))/SUM(ifnull(u.units,0)),2),0) AS average_price
FROM prices p
LEFT JOIN UnitsSold u
ON p.product_id = u.product_id
WHERE u.purchase_date >= start_date
AND u.purchase_date <= end_date or p.product_id is null or purchase_date is null or units is null
GROUP BY  p.product_id