SELECT  employee_id
       ,if(employee_id %2 = 0 or name LIKE 'M%',salary*0,salary) AS bonus
FROM Employees
ORDER BY employee_id