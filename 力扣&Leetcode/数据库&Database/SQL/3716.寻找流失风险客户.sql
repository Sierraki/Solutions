with
    a1 as (
        select
            *,
            row_number() over (
                partition by
                    user_id
                order by
                    event_date desc
            ) num2,
            min(event_date) over (
                partition by
                    user_id
            ) start,
            max(event_date) over (
                partition by
                    user_id
            ) end,
            max(monthly_amount) over (
                partition by
                    user_id
            ) mx
        from
            subscription_events
    ),
    a2 as (
        select
            user_id,
            plan_name current_plan,
            monthly_amount current_monthly_amount,
            mx max_historical_amount,
            timestampdiff(day, start, end) days_as_subscriber
        from
            a1
        where
            num2 = 1
            and event_type != 'cancel'
            and monthly_amount < mx * 0.5
            and timestampdiff(day, start, end) >= 60
    )
select
    *
from
    a2
where
    user_id in (
        select
            user_id
        from
            a1
        where
            event_type = 'downgrade'
        group by
            user_id
        having
            count(*) >= 1
    )
order by
    days_as_subscriber desc,
    user_id asc