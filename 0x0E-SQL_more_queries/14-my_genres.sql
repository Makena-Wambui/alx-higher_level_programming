-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
SELECT A.name
FROM tv_genres A
INNER JOIN tv_show_genres B
ON A.id = B.genre_id
INNER JOIN tv_shows C
ON C.id = B.show_id
WHERE C.title = 'Dexter'
ORDER BY name
;
