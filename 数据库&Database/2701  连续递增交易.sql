/* 先筛出连续天 再筛大于0 再筛连续天 */
WITH aa AS
(
	SELECT  transaction_id
	       ,customer_id
	       ,transaction_date
	       ,SUM(amount) amount
	FROM Transactions
	GROUP BY  customer_id
	         ,transaction_date
) , a1 AS
(
	SELECT  transaction_id tid
	       ,customer_id id
	       ,transaction_date d
	       ,amount a
	FROM aa
) , a2 as(
SELECT  id
       ,d
       ,lead(d)over(PARTITION BY id ORDER BY  d) d1
       ,a
       ,lead(a)over(PARTITION BY id ORDER BY d) a1
FROM a1) , a3 AS
(
	SELECT  id
	       ,d
	       ,d1
	       ,a
	       ,a1
	       ,timestampdiff(day,d,d1) timed
	       ,a1-a ad
	FROM a2
	WHERE ( timestampdiff(day, d, d1) = 1 AND a1-a > 0 ) 
) , a4 AS
(
	SELECT  id
	       ,d
	       ,to_days(d)-ROW_NUMBER()over(PARTITION BY id ORDER BY  d)num
	FROM a3
) , a5 AS
(
	SELECT  *
	       ,COUNT(*)over(PARTITION BY id,num)+1 cnt
	       ,MIN(d)over(PARTITION BY id,num) mi
	       ,MAX(d)over(PARTITION BY id,num) ma
	FROM a4
)
SELECT  distinct id customer_id
       ,mi consecutive_start
       ,date_add(ma,interval 1 day) consecutive_end
FROM a5
WHERE cnt >= 3
ORDER BY customer_id 