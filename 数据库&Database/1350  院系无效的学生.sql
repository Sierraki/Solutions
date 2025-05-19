SELECT  s.id
       ,s.name
FROM Students s
LEFT JOIN departments d
ON s.department_id = d.id
WHERE d.name is null