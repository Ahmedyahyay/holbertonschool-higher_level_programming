-- This script lists all genres linked to the TV show titled 'Dexter'
-- It selects genre names from the genres table filtered by the show's title
-- Results are sorted in ascending order by genre name
-- Uses JOIN between tv_shows, tv_show_genres, and genres tables
-- The database name will be passed as an argument to the mysql command

SELECT genres.name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;

