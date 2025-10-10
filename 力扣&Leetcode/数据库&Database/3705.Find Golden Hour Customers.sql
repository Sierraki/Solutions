# 总人数
with
    a1 as (
        select
            customer_id,
            count(*) total_cnt
        from
            restaurant_orders
        group by
            customer_id
    )
    # 高峰时段人数
,
    a2 as (
        select
            customer_id,
            count(*) goal_cnt
        from
            restaurant_orders
        where
            (
                TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
                or TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
            )
        group by
            customer_id
    ),
    # 平均分
    a3 as (
        select
            customer_id,
            round(avg(ifnull(order_rating, 0)), 2) avg_rat
        from
            restaurant_orders
        where
            order_rating is not null
        group by
            customer_id
    )
    # 评级计数
,
    a4 as (
        select
            customer_id,
            count(*) rat_cnt
        from
            restaurant_orders
        where
            order_rating is not null
        group by
            customer_id
    )
select
    customer_id,
    total_cnt total_orders,
    round(ifnull(goal_cnt, 0) / total_cnt * 100) peak_hour_percentage,
    avg_rat average_rating
from
    a1
    left join a2 using (customer_id)
    left join a3 using (customer_id)
    left join a4 using (customer_id)
where
    total_cnt >= 3
    and round(ifnull(goal_cnt, 0) / total_cnt) >= 0.6
    and avg_rat >= 4.0
    and rat_cnt / total_cnt > 0.5
order by
    avg_rat desc,
    customer_id desc