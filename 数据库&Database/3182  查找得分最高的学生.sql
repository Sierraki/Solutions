with
    a1 as (
        select
            student_id,
            major,
            course_id
        from
            students
            cross join courses using (major)
    ),
    a2 as (
        select
            student_id,
            major,
            course_id,
            grade
        from
            a1
            left join enrollments using (student_id, course_id)
    )
select distinct
    student_id
from
    a2
where
    student_id not in (
        select
            student_id
        from
            a2
        where
            grade <> 'A'
            or grade is null
    )
order by
    student_id