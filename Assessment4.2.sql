USE foundation_assessment_ii;

SELECT movie_info.movie_name, showings.start_time
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
WHERE showings.start_time > '12:00'
AND showings.available_seats > 0
ORDER BY showings.start_time;