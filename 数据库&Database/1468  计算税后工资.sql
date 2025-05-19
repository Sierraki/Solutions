WITH a1 AS
(
	SELECT  *
	       ,MAX(salary) OVER (PARTITION BY company_id) A
	FROM salaries
), a2 AS
(
	SELECT  *
	       ,CASE WHEN A < 1000 THEN 0
	             WHEN A BETWEEN 1000 AND 10000 THEN 24  ELSE 49 END AS tax
	FROM a1
)
SELECT  company_id
       ,employee_id
       ,employee_name
       ,round(salary-salary*tax/100,0) salary
FROM a2