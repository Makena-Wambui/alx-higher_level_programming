-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Only one SELECT statement
-- If a show doesn’t have a genre, display NULL
-- Use a LEFT OUTER JOIN clause, IS NULL to achieve this
SELECT A.title, B.genre_id
FROM tv_shows A
LEFT JOIN tv_show_genres AS B
ON A.id = B.show_id
WHERE B.genre_id IS NULL
ORDER BY A.title, B.genre_id;
