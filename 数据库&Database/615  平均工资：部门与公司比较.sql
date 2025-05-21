WITH s1 AS
(
	SELECT  date_format(pay_date,'%Y-%m') AS time
	       ,AVG(amount)as avgA
	FROM salary
	GROUP BY  date_format(pay_date,'%Y-%m')
)
SELECT  pay_month
       ,d department_id
       ,CASE WHEN Eavg > avgA THEN 'higher'
             WHEN Eavg < avgA THEN 'lower'  ELSE 'same' END AS comparison
FROM
(
	SELECT  department_id d
	       ,pay_month
	       ,AVG(amount) OVER (PARTITION BY pay_month,department_id)  AS Eavg
	       ,ROW_NUMBER() OVER (PARTITION BY pay_month,department_id) AS id
	FROM
	(
		SELECT  e.department_id
		       ,s.amount
		       ,date_format(s.pay_date,'%Y-%m')as pay_month
		FROM Salary s
		LEFT JOIN Employee e
		ON s.employee_id = e.employee_id
	)t1
)t2
LEFT JOIN s1
ON t2.pay_month = s1.time
WHERE id = 1