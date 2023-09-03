# INF115 Crash course

## Select
''' sql
SELECT director, COUNT(*) as c -- Kolonner
FROM movie -- Tabeller
WHERE country = "Dabendorf" -- Betingelser
GROUP BY director -- Gruppering etter kolonner
HAVING c > 3 -- Betingelser etter grupper
ORDER BY c DESC -- Sortering etter kolonner
LIMIT 3; -- Velg de første n output linjene
'''

## Insert
''' sql
INSERT INTO movie (title, director, year, country, minutes, rating, votes, budget, gross)
VALUES ("The Room", "Tommy Wiseau", 2003, "USA", 99, 3.7, 160000, 6000000, 1800);
'''
