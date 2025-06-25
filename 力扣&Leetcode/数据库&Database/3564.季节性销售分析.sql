with
    a1 as (
        select
            case
                when month(sale_date) in (12, 1, 2) then 'Winter'
                when month(sale_date) in (3, 4, 5) then 'Spring'
                when month(sale_date) in (6, 7, 8) then 'Summer'
                when month(sale_date) in (9, 10, 11) then 'Fall'
            end as season,
            product_id,
            category,
            quantity,
            price
        from
            sales
            left join products using (product_id)
    ),
    a2 as (
        select
            season,
            category,
            sum(quantity) cnt,
            sum(price * quantity) total
        from
            a1
        group by
            season,
            category
        order by
            season
    ),
    a3 as (
        select
            *,
            row_number() over (
                partition by
                    season
                order by
                    cnt desc,
                    total desc
            ) num
        from
            a2
    )
select
    season,
    category,
    cnt total_quantity,
    total total_revenue
from
    a3
where
    num = 1
order by
    season