WITH
	a1 AS (
		SELECT
			*,
			timestampdiff (second, entry_time, exit_time) / 3600 hdiff
		FROM
			ParkingTransactions
	),
	a2 AS (
		SELECT
			car_id,
			lot_id,
			SUM(fee_paid) tfee,
			SUM(hdiff) thour,
			ROW_NUMBER() over (
				PARTITION BY
					car_id
				ORDER BY
					SUM(hdiff) desc
			) r
		FROM
			a1
		GROUP BY
			car_id,
			lot_id
		ORDER BY
			car_id
	),
	a3 AS (
		SELECT
			car_id,
			lot_id most_time_lot
		FROM
			a2
		WHERE
			r = 1
	) /*most_time_lot*/,
	a4 AS (
		SELECT
			car_id,
			SUM(tfee) total_fee_paid,
			round(SUM(tfee) / SUM(thour), 2) avg_hourly_fee
		FROM
			a2
		GROUP BY
			car_id
	)
SELECT
	car_id,
	total_fee_paid,
	avg_hourly_fee,
	most_time_lot
FROM
	a3
	LEFT JOIN a4 USING (car_id)