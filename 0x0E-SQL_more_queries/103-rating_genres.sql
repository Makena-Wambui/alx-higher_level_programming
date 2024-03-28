-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by the rating
-- only one SELECT statement
SELECT A.name,
SUM(rate) rating
FROM tv_genres A
INNER JOIN  tv_show_genres B
ON A.id = B.genre_id
INNER JOIN tv_show_ratings C
ON B.show_id = C.show_id
GROUP BY A.name
ORDER BY rating DESC;
;
