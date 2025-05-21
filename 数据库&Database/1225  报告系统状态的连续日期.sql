WITH a1 AS
(
	SELECT  fail_date d1
	       ,'failed' stat
	       ,ROW_NUMBER() OVER (order by fail_date ASC) A
	FROM failed
	WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31' 
	UNION ALL
	SELECT  success_date d1
	       ,'succeeded' stat
	       ,ROW_NUMBER() OVER (order by success_date ASC)-1 A
	FROM Succeeded
	WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
	ORDER BY d1 ASC 
), a2 AS
(
	SELECT  d1
	       ,stat
	       ,A
	       ,ROW_NUMBER() OVER (order by d1 ASC) num
	       ,ROW_NUMBER() OVER (order by d1 ASC)-A cc
	FROM a1
), a3 AS
(
	SELECT  d1
	       ,stat
	       ,A
	       ,num
	       ,cc
	       ,MIN(d1) OVER (PARTITION BY cc,stat ) m1
	       ,MAX(d1) OVER (PARTITION BY cc,stat ) m2
	FROM a2
	ORDER BY d1
)
SELECT  stat period_state
       ,m1 start_date
       ,m2 end_date
FROM a3
GROUP BY  m1