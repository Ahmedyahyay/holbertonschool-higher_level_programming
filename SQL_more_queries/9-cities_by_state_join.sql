-- This script lists all cities in the hbtn_0d_usa database
-- For each city, it displays the city's id, city name, and the corresponding state name
-- The results are sorted by cities.id in ascending order
-- Only one SELECT statement is used with an INNER JOIN between cities and states

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;

