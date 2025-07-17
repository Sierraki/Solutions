with
    a1 as (
        select
            employee_id,
            sum(duration_hours) hours,
            date_format(meeting_date, '%u') num
        from
            meetings
        group by
            employee_id,
            num
    ),
    a2 as (
        select
            *,
            count(*) over (
                partition by
                    employee_id
            ) cnt
        from
            a1
        where
            hours > 20
    ),
    a3 as (
        select
            employee_id,
            cnt meeting_heavy_weeks
        from
            a2
        where
            cnt >= 2
    )
select distinct
    employee_id,
    employee_name,
    department,
    meeting_heavy_weeks
from
    a3
    left join employees using (employee_id)
order by
    meeting_heavy_weeks desc,
    employee_name