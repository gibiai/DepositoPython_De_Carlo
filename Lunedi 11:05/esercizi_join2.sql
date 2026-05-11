# Esercizio 1
SELECT libri.titolo, libri.autore, vendite.data_vendita, vendite.negozio
FROM libri
INNER JOIN vendite
ON libri.id = vendite.id_libro
WHERE libri.autore LIKE '%King%';

# Esercizio 2
SELECT libri.titolo, libri.anno_pubblicazione, libri.prezzo, vendite.data_vendita
FROM libri
LEFT JOIN vendite
ON libri.id = vendite.id_libro
WHERE libri.anno_pubblicazione BETWEEN 2000 AND 2010;

# Esercizio 3
SELECT libri.titolo, vendite.negozio, vendite.quantita, vendite.quantita * libri.prezzo AS prezzo_totale
FROM libri
INNER JOIN vendite
ON libri.id = vendite.id_libro
WHERE vendite.negozio IN (
    '9 Oriole Lane',
    '98558 Milwaukee Point',
    '98016 Esch Trail'
);

# Esercizio 4
SELECT libri.titolo, vendite.data_vendita, libri.prezzo, vendite.quantita
FROM libri
RIGHT JOIN vendite
ON libri.id = vendite.id_libro
WHERE vendite.data_vendita BETWEEN '2020-01-01' AND '2022-12-31'
AND vendite.negozio LIKE '%Drive%';

# Esercizio 5
SELECT libri.titolo, libri.autore, libri.prezzo, vendite.data_vendita
FROM libri
INNER JOIN vendite ON libri.id = vendite.id_libro
WHERE libri.genere IN ('Fantasy', 'Horror', 'Drama')
AND libri.anno_pubblicazione > 2015
AND vendite.negozio LIKE '%Plaza%'
ORDER BY vendite.data_vendita DESC;


-- SELECT COUNT(*) 
-- FROM libri
-- WHERE libri.genere IN ('Fantasy', 'Horror', 'Drama')
-- AND libri.anno_pubblicazione > 2015;

-- SELECT libri.titolo, libri.genere, libri.anno_pubblicazione, vendite.negozio
-- FROM libri
-- INNER JOIN vendite ON libri.id = vendite.id_libro
-- WHERE libri.genere IN ('Fantasy', 'Horror', 'Drama')
-- AND libri.anno_pubblicazione > 2015;


