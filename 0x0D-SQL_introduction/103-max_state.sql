-- max temp
SELECT state, MAX(value) as max_temp
FROM temperatures
ORDER BY state ASC
