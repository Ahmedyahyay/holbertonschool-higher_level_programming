-- This script lists all TV shows from the hbtn_0d_tvshows database
-- It displays the show title and genre_id for shows that have at least one linked genre
-- Results are sorted by show title and genre_id in ascending order
-- Only one SELECT statement is used with an INNER JOIN between tv_shows and tv_show_genres

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

