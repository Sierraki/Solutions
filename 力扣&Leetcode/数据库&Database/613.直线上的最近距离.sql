SELECT  MIN(ABS(t1.x - t2.x)) AS shortest
FROM point t1
CROSS JOIN point t2
WHERE t1.x <> t2.x