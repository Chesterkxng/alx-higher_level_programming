-- all genre of dexter
SELECT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres
INNER JOIN tv_shows
ON tv_genres.id=tv_show_genres.genre_id
AND tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;
