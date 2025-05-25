SELECT  activity_date           AS day
       ,COUNT(distinct user_id) AS active_users
FROM Activity
WHERE date(activity_date) BETWEEN date_sub('2019-07-27', interval 29 day) AND '2019-07-27'
GROUP BY  activity_date