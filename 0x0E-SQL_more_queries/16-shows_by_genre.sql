-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- only one SELECT statement
SELECT A.title, C.name
FROM tv_shows A
LEFT OUTER JOIN tv_show_genres B
ON A.id = B.show_id
LEFT OUTER JOIN tv_genres C
ON B.genre_id = C.id
ORDER BY A.title, C.name
;
