-- a script that lists all cities contained in the database
SELECT cities.id as id, cities.name as name, states.name as name
FROM cities INNER JOIN states
ON cities.state_id = states.id;
ORDER BY cities.id ASC;
