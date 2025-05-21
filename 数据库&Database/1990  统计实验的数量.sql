WITH a1 AS
(
	SELECT  'Android' platform
	UNION
	SELECT  'IOS'
	UNION
	SELECT  'Web'
), a2 AS
(
	SELECT  'Reading' experiment_name
	UNION
	SELECT  'Sports'
	UNION
	SELECT  'Programming'
), a3 AS
(
	SELECT  platform
	       ,experiment_name
	       ,COUNT(*) num_experiments
	FROM Experiments
	GROUP BY  platform
	         ,experiment_name
), a4 AS
(
	SELECT  a1.platform
	       ,a2.experiment_name
	       ,0 'num_experiments'
	FROM a1
	CROSS JOIN a2
)
SELECT  a4.platform
       ,a4.experiment_name
       ,ifnull(a3.num_experiments,0) num_experiments
FROM a4
LEFT JOIN a3
ON a4.platform = a3.platform AND a4.experiment_name = a3.experiment_name
ORDER BY a4.platform