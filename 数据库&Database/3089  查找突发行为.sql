WITH
	a AS (
		SELECT
			user_id
			-- ceiling(day(post_date)/7)                                                                         AS c1, 
,
			COUNT(1) over (
				PARTITION BY
					user_id
			) / 4 AS c2,
			COUNT(1) over (
				PARTITION BY
					user_id
				ORDER BY
					post_date range BETWEEN interval 6 day preceding
					AND current row
			) AS c3
		FROM
			Posts
		WHERE
			post_date BETWEEN '2024-02-01' AND '2024-02-28'
	)
SELECT
	user_id,
	MAX(c3) AS max_7day_posts,
	MAX(c2) AS avg_weekly_posts
FROM
	a
WHERE
	c2 * 2 <= c3
GROUP BY
	user_id
ORDER BY
	user_id