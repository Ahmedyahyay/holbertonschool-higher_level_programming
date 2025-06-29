-- This script lists all genres from the hbtn_0d_tvshows database
-- It displays each genre and the count of TV shows linked to it
-- Only genres with at least one linked show are displayed
-- Results are sorted in descending order by the number of shows linked
-- Uses a JOIN between tv_show_genres and genres, grouping by genre name

SELECT
  genres.name AS genre,
  COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;

