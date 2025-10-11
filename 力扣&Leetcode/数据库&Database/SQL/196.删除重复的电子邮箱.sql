delete
FROM person
WHERE id NOT IN ( SELECT t1.id FROM  ( SELECT MIN (id) AS id FROM person GROUP BY email  ) AS t1) 