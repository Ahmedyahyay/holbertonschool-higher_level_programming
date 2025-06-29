-- This script lists all TV shows from the hbtn_0d_tvshows database
-- It displays the show title and genre_id for all shows, including those without any genre
-- Shows without a genre will display NULL for genre_id
-- Results are sorted by show title and genre_id in ascending order
-- Only one SELECT statement is used with a LEFT JOIN to include all shows

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

