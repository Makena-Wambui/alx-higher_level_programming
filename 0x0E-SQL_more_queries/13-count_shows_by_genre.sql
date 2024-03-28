-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement
-- If a show doesn’t have a genre, display NULL
-- Use a LEFT OUTER JOIN clause, IS NULL to achieve this
SELECT A.name genre,
COUNT(*) number_of_shows
FROM tv_genres A
INNER JOIN tv_show_genres B
ON A.id = B.genre_id
GROUP BY A.name
ORDER BY number_of_shows DESC
;
