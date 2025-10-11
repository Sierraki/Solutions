with
    a1 as (
        select
            driver_id,
            (distance_km / fuel_consumed) res,
            case
                when month(trip_date) <= 6 then 'a'
                else 'b'
            end as half
        from
            trips
    ),
    a2 as (
        select
            *,
            count(*) over (
                partition by
                    driver_id,
                    half
            ) cnt
        from
            a1
    )
    # first
,
    a3 as (
        select
            driver_id,
            sum(res / cnt) res1
        from
            a2
        where
            half = 'a'
        group by
            driver_id
    )
    # second
,
    a4 as (
        select
            driver_id,
            sum(res / cnt) res2
        from
            a2
        where
            half = 'b'
        group by
            driver_id
    )
select
    driver_id,
    driver_name,
    round(res1, 2) first_half_avg,
    round(res2, 2) second_half_avg,
    round(res2 - res1, 2) efficiency_improvement
from
    a3
    left join a4 using (driver_id)
    left join drivers using (driver_id)
where
    res2 is not null
    and res1 is not null
    and res2 - res1 > 0
order by
    efficiency_improvement desc,
    driver_name