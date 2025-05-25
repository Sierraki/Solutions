WITH
	a1 AS (
		SELECT
			N,
			'Leaf' as Type
		FROM
			tree
		WHERE
			P is not null
			AND N NOT IN(
				SELECT
					P
				FROM
					tree
				WHERE
					P is not null
			)
	) /*leaf*/,
	a2 AS (
		SELECT
			N,
			'Root' Type
		FROM
			tree
		WHERE
			p is null
	) /*root*/
SELECT
	N,
	'Inner' Type
FROM
	tree
WHERE
	P is not null
	AND N NOT IN(
		SELECT
			N
		FROM
			a1
	)
UNION
SELECT
	*
FROM
	a1
UNION
SELECT
	*
FROM
	a2
ORDER BY
	N