SELECT  id
       ,company
       ,salary
FROM
(
	SELECT  id
	       ,company
	       ,salary
	       ,ROW_NUMBER() over(PARTITION BY company ORDER BY  salary ASC) rankk
	       ,COUNT(id) over(PARTITION BY company) num
	FROM employee
)t1
WHERE rankk >= num/2
AND rankk <= num/2+1