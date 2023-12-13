-- all genre of dexter
SELECT tv_shows.title AS title
FROM tv_shows
INNER JOIN tv_show_genres
INNER JOIN tv_genres
ON tv_genres.id=tv_show_genres.genre_id
AND tv_shows.id=tv_show_genres.show_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
