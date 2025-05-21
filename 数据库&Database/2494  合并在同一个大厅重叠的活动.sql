WITH a1 AS
(
	SELECT  *
	       ,MAX(end_day)over(PARTITION BY hall_id ORDER BY  start_day rows BETWEEN unbounded preceding AND 1 preceding ) A
	FROM hallevents
) , a2 AS
(
	SELECT  *
	       ,CASE WHEN A >= start_day or A is null THEN 0 /*no OVER lap*/  ELSE 1/*overlap*/ END AS ol
	FROM a1
) , a3 AS
(
	SELECT  *
	       ,SUM(ol)over(PARTITION BY hall_id ORDER BY  start_day) cnt
	FROM a2
)
SELECT  distinct hall_id
       ,MIN(start_day)over(PARTITION BY hall_id,cnt) start_day
       ,MAX(end_day)over(PARTITION BY hall_id,cnt) end_day
FROM a3