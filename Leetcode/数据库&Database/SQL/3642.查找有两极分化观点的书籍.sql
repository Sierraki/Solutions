# 超过五次阅读
with
    a1 as (
        select
            book_id
        from
            reading_sessions
        group by
            book_id
        having
            count(*) >= 5
    ),
    a2 as (
        select distinct
            book_id,
            max(session_rating) over (
                partition by
                    book_id
            ) mx,
            min(session_rating) over (
                partition by
                    book_id
            ) mi,
            count(*) over (
                partition by
                    book_id
            ) total_cnt
        from
            reading_sessions
    )
    # po
,
    a3 as (
        select
            book_id,
            count(*) cnt1
        from
            reading_sessions
        where
            session_rating >= 4
            or session_rating <= 2
        group by
            book_id
    ),
    a4 as (
        select distinct
            book_id
        from
            reading_sessions
        where
            session_rating >= 4
    ),
    a5 as (
        select distinct
            book_id
        from
            reading_sessions
        where
            session_rating <= 2
    )
select
    book_id,
    title,
    author,
    genre,
    books.pages,
    mx - mi rating_spread,
    round(cnt1 / total_cnt, 2) polarization_score
from
    a2
    left join a3 using (book_id)
    left join books using (book_id)
where
    cnt1 is not null
    and cnt1 / total_cnt >= 0.6
    and book_id in (
        select
            book_id
        from
            a1
    )
    and book_id in (
        (
            select
                book_id
            from
                a4
        )
    )
    and book_id in (
        (
            select
                book_id
            from
                a5
        )
    )
order by
    polarization_score desc,
    title desc