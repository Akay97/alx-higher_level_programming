-- A script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).
CREATE TABLE IF NOT EXISTS temp_July_Aug
       SELECT *
       FROM temperatures
       WHERE month = 7 OR month = 8;
SELECT city, AVG(value) AS avg_temp
FROM temp_July_Aug
GROUP BY city
ORDER BY avg_temp DESC
limit 3;
