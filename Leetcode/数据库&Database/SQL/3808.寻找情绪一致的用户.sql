select
    user_id,
    reaction dominant_reaction,
    round(cnt / total_cnt, 2) reaction_ratio
from
    (
        select distinct
            user_id,
            reaction,
            count(*) over (
                partition by
                    user_id,
                    reaction
            ) cnt,
            count(*) over (
                partition by
                    user_id
            ) total_cnt
        from
            reactions
    ) t1
where
    cnt / total_cnt >= 0.6
    and user_id in (
        select distinct
            user_id
        from
            reactions
        group by
            user_id
        having
            count(*) >= 5
    )
order by
    reaction_ratio desc,
    user_id