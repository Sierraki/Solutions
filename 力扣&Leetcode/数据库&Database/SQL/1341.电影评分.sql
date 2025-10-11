SELECT  *
FROM
(
	SELECT  a.name AS results
	FROM
	(
		SELECT  t1.user_id
		       ,t1.name
		       ,COUNT(*) AS cnt
		FROM Users t1
		JOIN MovieRating t2
		ON t1.user_id = t2.user_id
		GROUP BY  t1.user_id
		         ,t1.name
	) a
	ORDER BY a.cnt desc, a.name
	LIMIT 1
) tmp
UNION ALL
SELECT  *
FROM
(
	SELECT  a.title AS results
	FROM
	(
		SELECT  t1.movie_id
		       ,t1.title
		       ,AVG(t2.rating) AS avgNum
		FROM Movies t1
		JOIN MovieRating t2
		ON t1.movie_id = t2.movie_id
		WHERE date_format(t2.created_at, '%Y-%m') = '2020-02'
		GROUP BY  t1.movie_id
		         ,t1.title
	) a
	ORDER BY a.avgNum desc, a.title
	LIMIT 1
) tmp;