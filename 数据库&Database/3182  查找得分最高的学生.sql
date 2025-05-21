WITH
  a1 AS (
    SELECT
      student_id,
      major,
      course_id
    FROM
      students
      CROSS JOIN courses USING (major)
  ),
  a2 AS (
    SELECT
      student_id,
      major,
      course_id,
      grade
    FROM
      a1
      LEFT JOIN enrollments USING (student_id, course_id)
  )
SELECT distinct
  student_id
FROM
  a2
WHERE
  student_id NOT IN (
    SELECT
      student_id
    FROM
      a2
    WHERE
      grade <> 'A'
      or grade is null
  )
ORDER BY
  student_id