-- This script lists all the cities in California from the hbtn_0d_usa database
-- It uses a subquery to get the state_id of California without using JOIN
-- Results are sorted by cities.id in ascending order

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

