WITH a1 AS
(
	SELECT  customer_id
	       ,product_id
	       ,amount
	       ,category
	       ,price
	       ,transaction_date
	       ,round(SUM(amount)over(PARTITION BY customer_id),2) total_amount
	       ,COUNT(*)over(PARTITION BY customer_id) transaction_count
	       ,round(AVG(amount)over(PARTITION BY customer_id),2) avg_transaction_amount
	       ,COUNT(*)over(PARTITION BY customer_id,category ) categorycount
	FROM transactions
	LEFT JOIN products using
	(product_id
	)
) , a2 AS
(
	SELECT  *
	       ,ROW_NUMBER()over(PARTITION BY customer_id ORDER BY  categorycount desc,transaction_date DESC ) r
	FROM a1
) , a3 AS
(
	SELECT  customer_id
	       ,category top_category
	FROM a2
	WHERE r = 1
)/*top_category*/ , a4 AS (
SELECT  customer_id
       ,COUNT(distinct category) unique_categories
FROM a1
GROUP BY  customer_id)/*unique_categories*/
SELECT  distinct customer_id
       ,total_amount
       ,transaction_count
       ,unique_categories
       ,avg_transaction_amount
       ,top_category
       ,round((transaction_count*10)+(total_amount/100),2) loyalty_score
FROM a1
LEFT JOIN a4 using
(customer_id
)
LEFT JOIN a3 using
(customer_id
)
ORDER BY loyalty_score desc, customer_id