SELECT  t1.question_id AS survey_log
FROM
(
	SELECT  action
	       ,question_id
	       ,COUNT(*)over(PARTITION BY question_id)as show_count
	FROM SurveyLog
	WHERE action = 'show' 
)t1
LEFT JOIN
(
	SELECT  action
	       ,question_id
	       ,COUNT(*)over(PARTITION BY question_id)as answer_count
	FROM SurveyLog
	WHERE action = 'answer' 
)t2
ON t1.question_id = t2.question_id
ORDER BY ifnull(t2.answer_count, 0)/t1.show_count DESC
LIMIT 1