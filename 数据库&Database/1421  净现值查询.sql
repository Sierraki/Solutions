SELECT  q.id
       ,q.year
       ,ifnull(n.npv,0) npv
FROM queries q
LEFT JOIN npv n
ON q.id = n.id AND n.year = q.year