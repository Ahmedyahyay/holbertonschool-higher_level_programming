-- This script lists all TV shows from the hbtn_0d_tvshows database
-- It displays only shows without any genre linked (genre_id is NULL)
-- Results are sorted by show title and genre_id in ascending order
-- Uses a LEFT JOIN and filters for NULL genre_id to find shows with no genre
-- Only one SELECT statement is used

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

