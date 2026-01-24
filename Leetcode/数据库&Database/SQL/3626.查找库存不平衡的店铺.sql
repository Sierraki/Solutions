with
    a1 as (
        select
            store_id
        from
            inventory
        group by
            store_id
        having
            count(*) >= 3
    ),
    a2 as (
        select
            *
        from
            inventory
        where
            store_id in (
                select
                    store_id
                from
                    a1
            )
    )
    # 最贵 a4
,
    a3 as (
        select
            store_id,
            product_name p1,
            quantity q1,
            price pri1,
            row_number() over (
                partition by
                    store_id
                order by
                    price desc,
                    quantity desc
            ) num
        from
            a2
    ),
    a4 as (
        select
            *
        from
            a3
        where
            num = 1
    )
    # 最便宜 a6
,
    a5 as (
        select
            store_id,
            product_name p2,
            quantity q2,
            price pri2,
            row_number() over (
                partition by
                    store_id
                order by
                    price,
                    quantity desc
            ) num
        from
            a2
    ),
    a6 as (
        select
            *
        from
            a5
        where
            num = 1
    )
select
    store_id,
    store_name,
    location,
    p1 most_exp_product,
    p2 cheapest_product,
    round(q2 / q1, 2) imbalance_ratio
from
    a4
    left join a6 using (store_id)
    left join stores using (store_id)
where
    q2 / q1 > 1
order by
    imbalance_ratio desc,
    store_name