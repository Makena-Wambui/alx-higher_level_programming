-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
-- only one SELECT statement
SELECT A.title,
SUM(rate) rating
FROM tv_shows A
INNER JOIN  tv_show_ratings B
ON A.id = B.show_id
GROUP BY A.title
ORDER BY rating DESC;
;
