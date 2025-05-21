SELECT  ad_id
       ,round(ifnull(clicks*100/(clicks+view),0),2) AS ctr
FROM
(
	SELECT  ad_id
	       ,SUM(if(action = 'Clicked',1,0)) AS clicks
	       ,SUM(if(action = 'Viewed',1,0))  AS view
	FROM Ads
	GROUP BY  ad_id
) tt
ORDER BY ctr desc, ad_id ASC