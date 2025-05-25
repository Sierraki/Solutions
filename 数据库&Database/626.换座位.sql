SELECT  CASE WHEN id%2 = 0 THEN id-1
             WHEN id%2 = 1 AND id <> (
SELECT  COUNT(*)as id
FROM seat ) THEN id+1 else id end AS id, student
FROM seat
ORDER BY id asc