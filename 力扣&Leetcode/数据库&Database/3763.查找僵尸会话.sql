# 超过三十分钟 a1
with
    a1 as (
        select
            user_id,
            count(*) cnt,
            timestampdiff(
                minute,
                min(event_timestamp),
                max(event_timestamp)
            ) dif
            #        min(event_timestamp) mi,
            #        max(event_timestamp) mx
        from
            app_events
        group by
            user_id
    )
    # scroll
,
    a2 as (
        select
            user_id,
            count(*) scroll_cnt
        from
            app_events
        where
            event_type = 'scroll'
        group by
            user_id
    )
    # click
,
    a3 as (
        select
            user_id,
            count(*) click_cnt
        from
            app_events
        where
            event_type = 'click'
        group by
            user_id
    )
    # purchase
,
    a4 as (
        select
            user_id,
            count(*) purchase_cnt
        from
            app_events
        where
            event_type = 'purchase'
        group by
            user_id
    ),
    res as (
        select
            user_id,
            session_id,
            cnt,
            dif,
            ifnull(scroll_cnt, 0) scroll_count,
            ifnull(click_cnt, 0) click_count,
            purchase_cnt
        from
            a1
            left join a2 using (user_id)
            left join a3 using (user_id)
            left join a4 using (user_id)
            left join (
                select distinct
                    user_id,
                    session_id
                from
                    app_events
            ) as t1 using (user_id)
    )
select
    session_id,
    user_id,
    dif session_duration_minutes,
    scroll_count
from
    res
where
    dif > 30
    and scroll_count >= 5
    and click_count / scroll_count < 0.2
    and purchase_cnt is null
order by
    scroll_count desc,
    session_id