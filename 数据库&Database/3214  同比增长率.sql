WITH a1 AS
(
	SELECT  year (transaction_date) year
	       ,product_id
	       ,SUM(spend) spend
	FROM user_transactions
	GROUP BY  product_id
	         ,year (transaction_date)
), a2 AS
(
	SELECT  *
	       ,lag (spend) OVER ( PARTITION BY product_id ORDER BY  year ) ps
	FROM a1
)
SELECT  year
       ,product_id
       ,spend curr_year_spend
       ,ps prev_year_spend
       ,round((spend - ps) / ps * 100,2) yoy_rate
FROM a2
ORDER BY product_id, year