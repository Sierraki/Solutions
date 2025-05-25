WITH a1 AS
(
	SELECT  date_format(purchase_date,'%V')-43 week_of_month
	       ,purchase_date
	       ,SUM(amount_spend) total_amount
	FROM purchases
	WHERE year(purchase_date) = 2023
	AND month(purchase_date) = 11
	AND date_format(purchase_date, '%w') = 5
	GROUP BY  date_format(purchase_date,'%V')-43
) , a2 AS
(
	SELECT  1            AS week_of_month
	       ,'2023-11-03' AS purchase_date
	UNION
	SELECT  2            AS week_of_month
	       ,'2023-11-10' AS purchase_date
	UNION
	SELECT  3            AS week_of_month
	       ,'2023-11-17' AS purchase_date
	UNION
	SELECT  4            AS week_of_month
	       ,'2023-11-24' AS purchase_date
)
SELECT  week_of_month
       ,purchase_date
       ,ifnull(total_amount,0)total_amount
FROM a2
LEFT JOIN a1 using
(week_of_month, purchase_date
)
ORDER BY week_of_month