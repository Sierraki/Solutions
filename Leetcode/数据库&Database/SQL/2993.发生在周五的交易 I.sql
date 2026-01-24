SELECT  date_format(purchase_date,'%v')-43 week_of_month
       ,purchase_date
       ,SUM(amount_spend) total_amount
FROM purchases
WHERE date_format(purchase_date, '%W') = 'Friday'
GROUP BY  purchase_date
ORDER BY  week_of_month