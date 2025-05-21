WITH
	a1 AS (
		SELECT
			date_format (purchase_date, '%V') -43 week_of_month,
			membership,
			SUM(amount_spend) total_amount
		FROM
			purchases
			LEFT JOIN users using (user_id)
		WHERE
			(
				membership = 'Premium'
				or membership = 'VIP'
			)
			AND date_format (purchase_date, '%w') = 5
		GROUP BY
			week_of_month,
			membership
	),
	a2 AS (
		SELECT
			1 AS week_of_month
		UNION
		SELECT
			2
		UNION
		SELECT
			3
		UNION
		SELECT
			4
	),
	a3 AS (
		SELECT
			'VIP' membership
		UNION
		SELECT
			'Premium'
	),
	a4 AS (
		SELECT
			*
		FROM
			a2,
			a3
	)
SELECT
	week_of_month,
	membership,
	ifnull (total_amount, 0) total_amount
FROM
	a4
	LEFT JOIN a1 using (week_of_month, membership)
ORDER BY
	week_of_month,
	membership