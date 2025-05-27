SELECT  machine_id
       ,round(AVG(time),3) AS processing_time
FROM
(
	SELECT  machine_id
	       ,process_id
	       ,SUM(time) AS time
	FROM
	(
		SELECT  machine_id
		       ,process_id
		       ,activity_type
		       ,if(activity_type = 'start',-1*timestamp,timestamp) AS time
		FROM Activity
	) AS t1
	GROUP BY  machine_id
	         ,process_id
) AS t2
GROUP BY  machine_id