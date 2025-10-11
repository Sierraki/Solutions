with
    a1 as (
        select
            student_id,
            session_date,
            lead(session_date) over (
                partition by
                    student_id
                order by
                    session_date
            ) nex
        from
            study_sessions
    ),
    a2 as (
        select
            student_id,
            session_date,
            timestampdiff(day, session_date, nex) dif
        from
            a1
    )
    # 超过两天的名单 需要移除
,
    r1 as (
        select distinct
            student_id
        from
            a2
        where
            dif > 2
    )
    # 小于6节课的名单 需要移除
,
    r2 as (
        select
            student_id
        from
            study_sessions
        group by
            student_id
        having
            count(*) < 6
    )
    # 计算循环次数 a4
,
    a33 as (
        select
            student_id,
            subject,
            count(*) over (
                partition by
                    student_id,
                    subject
            ) cnt
        from
            study_sessions
    ),
    a44 as (
        select
            student_id,
            subject,
            cnt,
            rank() over (
                partition by
                    student_id
                order by
                    cnt
            ) num
        from
            a33
    ),
    a3 as (
        select distinct
            student_id,
            cnt
        from
            a44
        where
            num = 1
    ),
    a4 as (
        select distinct
            student_id,
            cnt loop_cnt
        from
            study_sessions
            left join a3 using (student_id)
    )
    #
    # 计算单次循环持续时间 a6
,
    a5 as (
        select
            student_id,
            count(*) total_cnt
        from
            study_sessions
        group by
            student_id
    ),
    a6 as (
        select
            student_id,
            total_cnt / loop_cnt loop_time
        from
            a5
            left join a4 using (student_id)
        where
            student_id not in(
                select
                    *
                from
                    r1
                union
                select
                    *
                from
                    r2
            )
    )
    # 第一次处理 aa1
,
    aa1 as (
        select
            *
        from
            study_sessions
        where
            student_id not in(
                select
                    *
                from
                    r1
                union
                select
                    *
                from
                    r2
            )
    )
    # 计算时间 a7
,
    a7 as (
        select
            student_id,
            sum(hours_studied) total_hours
        from
            aa1
        group by
            student_id
    )
    # 验证每个loop是不是符合时间
,
    a8 as (
        select
            student_id,
            subject,
            session_date,
            row_number() over (
                partition by
                    student_id
                order by
                    session_date
            ) num
        from
            aa1
        order by
            student_id,
            subject
    ),
    a9 as (
        select
            student_id,
            subject,
            session_date,
            num,
            lead(num) over (
                partition by
                    student_id,
                    subject
                order by
                    session_date
            ) ne,
            round(loop_time, 0) loop_time
        from
            a8
            left join a6 using (student_id)
    )
    # 找出了不符合时间的名单 a10
,
    a10 as (
        select
            student_id
        from
            a9
        where
            ne is not null
            and ne - num <> loop_time
    )
    # 找出单个循环内不过三门的 a12
,
    a11 as (
        select distinct
            student_id,
            subject
        from
            aa1
    ),
    a12 as (
        select
            student_id
        from
            a11
        group by
            student_id
        having
            count(*) < 3
    )
select
    student_id,
    student_name,
    major,
    round(loop_time, 0) cycle_length,
    round(total_hours, 1) total_study_hours
from
    a6
    left join students using (student_id)
    left join a4 using (student_id)
    left join a7 using (student_id)
where
    student_id not in(
        select
            student_id
        from
            a12
    )
order by
    cycle_length desc,
    total_study_hours desc