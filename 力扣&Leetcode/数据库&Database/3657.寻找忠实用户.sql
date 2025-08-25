# Write your MySQL query statement below
-- 至少交易三次 a1
with
    a1 as (
        SELECT
            customer_id
        FROM
            customer_transactions
        WHERE
            transaction_type = 'purchase'
        group by
            customer_id
        HAVING
            COUNT(*) >= 3
    )
    -- 活跃至少30天 a5
,
    a2 as (
        SELECT
            customer_id,
            transaction_date,
            ROW_NUMBER() over (
                PARTITION BY
                    customer_id
                order by
                    transaction_date
            ) start,
            ROW_NUMBER() over (
                PARTITION BY
                    customer_id
                order by
                    transaction_date desc
            ) end
        FROM
            customer_transactions
    ),
    a3 as (
        SELECT
            customer_id,
            start,
            transaction_date s1
        FROM
            a2
        WHERE
            start = 1
    ),
    a4 as (
        SELECT
            customer_id,
            end,
            transaction_date e1
        FROM
            a2
        WHERE
            end = 1
    ),
    a5 as (
        SELECT
            customer_id
        from
            a3
            left join a4 USING (customer_id)
        where
            TIMESTAMPDIFF(day, s1, e1) >= 30
    )
    -- 退货率少于20% a9
,
    a6 as (
        SELECT
            customer_id,
            count(*) p_cnt
        from
            customer_transactions
        where
            transaction_type = 'purchase'
        group by
            customer_id
    ),
    a7 as (
        SELECT
            customer_id,
            count(*) r_cnt
        from
            customer_transactions
        where
            transaction_type = 'refund'
        group by
            customer_id
    ),
    a8 as (
        SELECT DISTINCT
            customer_id,
            p_cnt,
            ifnull(r_cnt, 0) r_cnt
        from
            customer_transactions
            left join a6 USING (customer_id)
            left join a7 USING (customer_id)
    ),
    a9 as (
        SELECT
            customer_id
        from
            a8
        WHERE
            r_cnt / p_cnt <= 0.2
    )
select
    customer_id
from
    a1
where
    customer_id in (
        select
            *
        from
            a5
    )
    and customer_id in (
        select
            *
        from
            a9
    )
order by
    customer_id
    # Write your MySQL query statement below
select
    customer_id
from
    customer_transactions
group by
    customer_id
having
    count(
        case
            when transaction_type = 'purchase' then transaction_id
            else null
        end
    ) >= 3
    and datediff(max(transaction_date), min(transaction_date)) >= 30
    and count(
        case
            when transaction_type = 'refund' then transaction_id
            else null
        end
    ) / count(distinct transaction_id) < 0.2
order by
    customer_id asc