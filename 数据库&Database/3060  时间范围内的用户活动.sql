WITH
	a1 AS (
		SELECT
			*,
			COUNT(*) oveR (
				PARTITION BY
					user_id,
					session_type
			) cnt,
			lead (session_start) oveR (
				PARTITION BY
					user_id,
					session_type
				ORDER BY
					session_start
			) ns
		FROM
			sessions
	)
SELECT distinct
	user_id
FROM
	a1
WHERE
	cnt >= 2
	AND timestampdiff (hour, session_end, ns) <= 12
ORDER BY
	user_id