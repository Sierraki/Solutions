# Write your MySQL query statement below
with
    a1 as (
        select
            user_id,
            avg(course_rating) avgg,
            count(*) cnt
        from
            course_completions
        group by
            user_id
    ),
    a2 as (
        select
            user_id
        from
            a1
        where
            cnt >= 5
            and avgg >= 4
    ),
    a3 as (
        select
            user_id id,
            course_name c1,
            lead(course_name) over (
                partition by
                    user_id
                order by
                    completion_date
            ) c2
        from
            course_completions
        where
            user_id in (
                select
                    user_id
                from
                    a2
            )
    )
select
    c1 first_course,
    c2 second_course,
    count(*) transition_count
from
    a3
where
    c2 is not null
group by
    c1,
    c2
order by
    transition_count desc,
    c1 asc,
    c2 asc