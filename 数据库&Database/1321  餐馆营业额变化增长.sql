WITH a1 AS
(
	SELECT  visited_on
	       ,SUM(amount) amount
	FROM customer
	GROUP BY  visited_on
), a2 AS
(
	SELECT  visited_on
	       ,SUM(amount) OVER (rows BETWEEN 6 preceding AND current row ) amount
	       ,ROW_NUMBER() OVER () num
	FROM a1
) /*每个日期前七天的总额*/
SELECT  visited_on
       ,amount
       ,round(amount/7,2)average_amount
FROM a2
WHERE num >= 7 