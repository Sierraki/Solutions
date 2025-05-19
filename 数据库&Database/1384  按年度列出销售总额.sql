WITH recursive a0 AS
(
	SELECT  MIN(year(period_start)) start
	FROM Sales
	UNION
	SELECT  start+1
	FROM a0
	WHERE start <= (
	SELECT  MAX(year(period_start))
	FROM sales )
	UNION
	SELECT  start+1
	FROM a0
	WHERE start <= (
	SELECT  MAX(year(period_end))
	FROM sales ) AND start BETWEEN '2019' AND '2020'
), a1 AS
(
	SELECT  *
	FROM a0
	WHERE start BETWEEN 2018 AND 2020 
), a2 as(
SELECT  concat(start,'-01-01') start
       ,concat(start,'-12-31') end
FROM a1), a3 AS
(
	SELECT  product_id
	       ,period_start
	       ,period_end
	       ,start
	       ,end
	FROM sales
	CROSS JOIN a2
	WHERE period_start BETWEEN start AND end or period_end BETWEEN start AND end or (period_start <= start AND period_end >= end)
	ORDER BY product_id
) -- ***** 
, a4 AS (
SELECT  *
       ,DATEDIFF(period_end,period_start)+1 AS A
       ,year(period_start) d1
FROM a3
GROUP BY  product_id
HAVING COUNT(*) = 1), /*卖了一年的东西的时间*/ a5 AS (
SELECT  *
       ,DATEDIFF(end,period_start)+1 A
       ,year(period_start) d1
FROM
(
	SELECT  *
	FROM a3
	WHERE period_start BETWEEN start AND end
)t1
WHERE product_id NOT IN ( SELECT product_id FROM a4 )), /*开始日期在时间段里面的*/ a6 AS (
SELECT  *
       ,DATEDIFF(period_end,start)+1 A
       ,year(period_end) d1
FROM
(
	SELECT  *
	FROM a3
	WHERE period_end BETWEEN start AND end
)t1
WHERE product_id NOT IN ( SELECT product_id FROM a4 )), /*结束日期在时间段里面的*/ a7 AS (
SELECT  *
       ,DATEDIFF(end,start)+1 A
       ,year(start) d1
FROM a3
WHERE period_start < start
AND period_end > end), /*全程在时间段里面的*/ a8 AS (
SELECT  *
FROM a4
UNION ALL
SELECT  *
FROM a5
UNION ALL
SELECT  *
FROM a6
UNION ALL
SELECT  *
FROM a7)
SELECT  a8.product_id
       ,product_name
       ,concat('',d1,'')report_year
       ,A*average_daily_sales total_amount
FROM a8
LEFT JOIN Sales s
ON a8.product_id = s.product_id
LEFT JOIN Product p
ON p.product_id = a8.product_id
ORDER BY product_id, d1