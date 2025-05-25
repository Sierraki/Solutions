SELECT  name
       ,bonus
FROM employee
LEFT JOIN bonus
ON employee.empid = bonus.empid
WHERE bonus is null or bonus < 1000 