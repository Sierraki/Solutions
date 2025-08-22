with
  a1 as (
    select
      patient_id,
      test_date,
      result,
      row_number() over (
        partition by
          patient_id,
          result
        order by
          test_date
      ) num
    from
      covid_tests
    where
      result = 'Negative'
      or result = 'Positive'
  )
  # positive
,
  a2 as (
    select
      *
    from
      a1
    where
      result = 'Positive'
      and num = 1
  ),
  a3 as (
    select
      patient_id,
      a2.test_date pd,
      a2.result pr,
      a1.test_date nd,
      a1.result nr,
      timestampdiff(day, a2.test_date, a1.test_date) recovery_time,
      row_number() over (
        partition by
          patient_id,
          a1.result
        order by
          a1.test_date
      ) num
    from
      a2
      left join a1 using (patient_id)
    where
      a1.result = 'negative'
      and a2.test_date < a1.test_date
  )
select
  patient_id,
  patient_name,
  age,
  recovery_time
from
  a3
  left join patients using (patient_id)
where
  num = 1
order by
  recovery_time,
  patient_name