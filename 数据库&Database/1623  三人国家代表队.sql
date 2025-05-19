WITH a1 AS
(
	SELECT  student_name A
	       ,B
	       ,C
	FROM SchoolA
	CROSS JOIN
	(
		SELECT  student_name B
		FROM SchoolB
	)t1
	CROSS JOIN
	(
		SELECT  student_name C
		FROM SchoolC
	)t2
), a2 AS
(
	SELECT  A
	       ,sa.student_id A1
	       ,B
	       ,sb.student_id B1
	       ,C
	       ,sc.student_id C1
	FROM a1
	LEFT JOIN SchoolA sa
	ON sa.student_name = a1.A
	LEFT JOIN SchoolB sb
	ON sb.student_name = a1.B
	LEFT JOIN SchoolC sc
	ON sc.student_name = a1.C
)
SELECT  A member_A
       ,B member_B
       ,C member_C
FROM a2
WHERE A <> B
AND B <> C
AND A <> C
AND A1 <> B1
AND B1 <> C1
AND A1 <> C1 