WITH
	a1 AS (
		SELECT
			*,
			ROW_NUMBER() over (
				PARTITION BY
					user_id
				ORDER BY
					session_start
			) r
		FROM
			sessions
	),
	a2 AS (
		SELECT
			user_id
		FROM
			a1
		WHERE
			r = 1
			AND session_type = 'Viewer'
	) /*list*/,
	a3 AS (
		SELECT
			user_id,
			COUNT(*) cnt
		FROM
			a1
		WHERE
			user_id IN (
				SELECT
					*
				FROM
					a2
			)
			AND session_type = 'Streamer'
		GROUP BY
			user_id
	) /*cnt*/
SELECT
	user_id,
	cnt sessions_count
FROM
	a2
	LEFT JOIN a3 using (user_id)
WHERE
	cnt is not null
ORDER BY
	sessions_count desc,
	user_id desc