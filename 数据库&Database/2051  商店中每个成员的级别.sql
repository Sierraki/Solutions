WITH a1 AS
(
	SELECT  member_id
	       ,COUNT(*) vcount
	FROM visits
	GROUP BY  member_id
), a2 AS
(
	SELECT  v.member_id
	       ,COUNT(*) pcount
	FROM Purchases p
	LEFT JOIN Visits v
	ON p.visit_id = v. visit_id
	GROUP BY  v.member_id
), a3 AS
(
	SELECT  m.member_id
	       ,ifnull(vcount,0) vcount
	FROM Members m
	LEFT JOIN a1
	ON m.member_id = a1.member_id
), /*访问次数*/ a4 AS (
SELECT  m.member_id
       ,name
       ,ifnull(pcount,0) pcount
       ,vcount
FROM Members m
LEFT JOIN a2
ON m.member_id = a2.member_id
LEFT JOIN a3
ON m.member_id = a3.member_id)
SELECT  member_id
       ,name
       ,CASE WHEN pcount/vcount >= 0.8 THEN 'Diamond'
             WHEN pcount/vcount >= 0.5 AND pcount/vcount < 0.8 THEN 'Gold'
             WHEN pcount/vcount < 0.5 THEN 'Silver'
             WHEN vcount = 0 THEN 'Bronze' END AS category
FROM a4