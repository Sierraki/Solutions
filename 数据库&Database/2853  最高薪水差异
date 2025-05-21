SELECT  abs(A-B) salary_difference
FROM
(
	SELECT  MAX(salary) A
	FROM salaries
	WHERE department = 'Engineering' 
)t1
CROSS JOIN
(
	SELECT  MAX(salary) B
	FROM salaries
	WHERE department = 'Marketing' 
)t2