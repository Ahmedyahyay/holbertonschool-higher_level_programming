-- This script lists all TV shows with their linked genres
-- Shows without any genre will display NULL in the genre column
-- Uses LEFT JOIN to include shows with no linked genres
-- Results are sorted ascending by show title and genre name
-- The database name will be passed as an argument to the mysql command

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

