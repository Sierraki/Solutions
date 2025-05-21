WITH
	a1 AS (
		SELECT
			id,
			MAX(height) over (
				rows BETWEEN unbounded preceding
				AND 1 preceding
			) l,
			height h,
			MAX(height) over (
				rows BETWEEN 1 following
				AND unbounded following
			) r
		FROM
			heights
		ORDER BY
			id
	),
	a2 as (
		SELECT
			*,
			CASE
				WHEN l = 0
				or r = 0 THEN 0
				WHEN h < l
				AND h < r
				AND r >= l THEN l - h
				WHEN h < l
				AND h < r
				AND l >= r THEN r - h
				WHEN r <= h
				or l <= h THEN 0
			END AS A
		FROM
			a1
		WHERE
			l is not null
			AND r is not null
	)
SELECT
	SUM(A) total_trapped_water
FROM
	a2