-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
-- You can use only one SELECT statement
SELECT A.title
FROM tv_shows A
INNER JOIN tv_show_genres B
ON A.id = B.show_id
INNER JOIN tv_genres C
ON B.genre_id = C.id
WHERE C.name = 'Comedy'
ORDER BY A.title
;
