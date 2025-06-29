-- This script lists all TV shows that belong to the 'Comedy' genre
-- It selects show titles from tv_shows filtered by genre 'Comedy'
-- Uses JOIN between tv_shows, tv_show_genres, and tv_genres tables
-- Results are sorted in ascending order by the show title
-- The database name will be passed as an argument to the mysql command

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;

