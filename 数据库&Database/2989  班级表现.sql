WITH a1 AS
(
	SELECT  student_id
	       ,assignment1+assignment2+assignment3 total
	       ,rank() OVER (order by assignment1+assignment2+assignment3 DESC)rankk
	FROM scores
), a2 AS
((
	SELECT  *
	FROM a1
	ORDER BY rankk
	LIMIT 1 )
	UNION ALL(
	SELECT  *
	FROM a1
	ORDER BY rankk DESC
	LIMIT 1 )
), a3 AS
(
	SELECT  total-lag(total)over (order by total) difference_in_score
	FROM a2
)
SELECT  *
FROM a3
WHERE difference_in_score is not null