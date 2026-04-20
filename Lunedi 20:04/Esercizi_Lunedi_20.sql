-- ESERCIZI: 

-- 1) DISTINCT e WHERE
SELECT DISTINCT Region
FROM Country
WHERE Continent = 'Europe';

-- 2) WHERE e ORDER BY
SELECT Name, Population
FROM City
WHERE CountryCode = 'USA' AND Population > 1000000
ORDER BY Population DESC;

-- 3) GROUP BY
SELECT Continent, COUNT(*), SUM(Population)
FROM Country
GROUP BY Continent
ORDER BY SUM(Population) DESC;