with
    a1 as (
        select
            student_id,
            major,
            course_id,
            credits,
            mandatory,
            grade,
            GPA
        from
            students
            left join courses using (major)
            left join enrollments using (course_id, student_id)
    ) /*list*/,
    a2 as (
        select
            *
        from
            a1
        where
            student_id not in (
                select
                    student_id
                from
                    a1
                where
                    (
                        mandatory = 'yes'
                        and grade is null
                    ) /*没有修必修课程*/
                    or (
                        mandatory = 'yes'
                        and grade <> 'A'
                    ) /*必修课程没有A*/
            )
    ) /*条件叠加*/,
    a3 as (
        select
            *,
            count(*) cnt
        from
            a2
        where
            grade is not null
            and mandatory = 'no'
        group by
            student_id
    ) /*选修的名单*/,
    a4 as (
        select
            student_id
        from
            a3
        where
            cnt >= 2
    ),
    a5 as (
        select
            *
        from
            a2
        where
            student_id in (
                select
                    *
                from
                    a4
            ) /*选修大于2的名单*/
    ),
    a6 as (
        select
            *
        from
            a3
        where
            grade in ('B', 'A')
    ),
    a7 as (
        select
            *
        from
            a5
        where
            student_id in (
                select
                    student_id
                from
                    a6
            ) /*选修至少B的名单*/
    ),
    a8 as (
        select
            student_id
        from
            enrollments
        group by
            student_id
        having
            avg(gpa) > 2.5
    ) /*超过2.5*/
select distinct
    student_id
from
    a7
where
    student_id in (
        select
            student_id
        from
            a8
    )
order by
    student_id