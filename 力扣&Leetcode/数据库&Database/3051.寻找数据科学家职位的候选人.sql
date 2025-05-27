WITH
	a1 AS (
		SELECT
			candidate_id A,
			skill s1
		FROM
			candidates
		WHERE
			skill = 'Python'
	),
	a2 AS (
		SELECT
			candidate_id B,
			skill s2
		FROM
			candidates
		WHERE
			skill = 'Tableau'
	),
	a3 AS (
		SELECT
			candidate_id C,
			skill s3
		FROM
			candidates
		WHERE
			skill = 'PostgreSQL'
	),
	a4 AS (
		SELECT
			*
		FROM
			a1
			LEFT JOIN a2 ON A = B
		WHERE
			B is not null
	)
SELECT
	A candidate_id
FROM
	a4
	LEFT JOIN a3 ON B = C
WHERE
	C is not null
ORDER BY
	A