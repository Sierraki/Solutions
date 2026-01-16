select distinct
    user_id,
    cnt prompt_count,
    round(avg, 2) avg_tokens
from
    (
        (
            select
                *,
                avg(tokens) over (
                    partition by
                        user_id
                ) avg,
                count(*) over (
                    partition by
                        user_id
                ) cnt
            from
                prompts
        )
    ) a1
where
    cnt >= 3
    and tokens > avg
order by
    avg_tokens desc,
    user_id