WITH a1 AS
(
	SELECT  caller_id id1
	FROM calls
	UNION
	SELECT  recipient_id
	FROM calls
)/*list*/ , a2 as(
SELECT  caller_id id1
       ,recipient_id id2
       ,call_time t
FROM calls
UNION
SELECT  recipient_id
       ,caller_id
       ,call_time
FROM calls) , a3 as(
SELECT  id1
       ,id2
       ,t
       ,ROW_NUMBER()over(PARTITION BY id1,date_format(t,'%Y-%m-%d') ORDER BY  t ) A
       ,ROW_NUMBER()over(PARTITION BY id1,date_format(t,'%Y-%m-%d') ORDER BY t DESC ) D
FROM a1
LEFT JOIN a2 using
(id1
) ) , a4 AS
(
	SELECT  id1
	       ,id2
	       ,date_format(t,'%Y-%m-%d')t
	FROM a3
	WHERE A = 1
) , a5 AS
(
	SELECT  id1
	       ,id2
	       ,date_format(t,'%Y-%m-%d')t
	FROM a3
	WHERE D = 1
) , a6 AS
(
	SELECT  a4.id1
	       ,a4.t
	       ,a4.id2
	       ,a5.id2 id3
	FROM a4
	LEFT JOIN a5
	ON a4.id1 = a5.id1 AND a4.t = a5.t
)
SELECT  distinct id1 user_id
FROM a6
WHERE id2 = id3