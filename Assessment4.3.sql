USE foundation_assessment_ii;

SELECT movie_info.movie_name, COUNT(showings.showing_ID) AS showings
FROM movie_info
JOIN showings ON movie_info.movie_ID = showings.movie_ID
GROUP BY movie_info.movie_name
ORDER BY Showings DESC
LIMIT 1;