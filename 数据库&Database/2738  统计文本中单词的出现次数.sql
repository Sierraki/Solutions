SELECT  'bull' word
       ,ifnull(COUNT(*),0) 'count'
FROM files
WHERE content LIKE '% bull %'
UNION
SELECT  'bear'
       ,ifnull(COUNT(*),0) 'count'
FROM files
WHERE content LIKE '% bear %'