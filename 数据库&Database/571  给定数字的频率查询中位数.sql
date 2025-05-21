SELECT  round(AVG(num),1) AS median
FROM
(
	SELECT  *
	       ,SUM(frequency)over(order by num ASC)-frequency+1 AS low
	       ,SUM(frequency)over(order by num ASC)             AS up
	       ,SUM(frequency)over()/2-0.5                       AS clow
	       ,SUM(frequency)over()/2+1.5                       AS cup
	FROM numbers
)t1
WHERE clow BETWEEN low AND up or cup BETWEEN low AND up 