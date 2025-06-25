with
    a1 as (
        select
            *,
            count(*) over (
                partition by
                    employee_id
            ) cnt,
            row_number() over (
                partition by
                    employee_id
                order by
                    review_date desc
            ) num
        from
            performance_reviews
    ),
    a2 as (
        select
            employee_id,
            review_date,
            rating,
            lead(rating) over (
                partition by
                    employee_id
                order by
                    review_date
            ) next
        from
            a1
        where
            cnt >= 3
            and num in (1, 2, 3)
        order by
            employee_id,
            review_date
    ),
    a3 as (
        select
            *,
            lead(next) over (
                partition by
                    employee_id
                order by
                    review_date
            ) nextnext
        from
            a2
    )
select
    employee_id,
    name,
    nextnext - rating improvement_score
from
    a3
    left join employees using (employee_id)
where
    rating < next
    and next < nextnext
order by
    improvement_score desc,
    name