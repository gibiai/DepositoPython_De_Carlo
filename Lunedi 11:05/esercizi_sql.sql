SELECT categoria, COUNT(*) AS numero_vendite
FROM Vendite
GROUP BY categoria;

SELECT categoria, AVG(prezzo_unitario) AS prezzo_medio
FROM Vendite
GROUP BY categoria;

SELECT prodotto, SUM(quantita) AS quantita_totale
FROM Vendite
GROUP BY prodotto;

SELECT MAX(prezzo_unitario) AS prezzo_massimo,
       MIN(prezzo_unitario) AS prezzo_minimo
FROM Vendite;

SELECT COUNT(*) AS totale_registrazioni
FROM Vendite;

SELECT prodotto, prezzo_unitario
FROM Vendite
ORDER BY prezzo_unitario DESC
LIMIT 5;

SELECT prodotto, SUM(quantita) AS quantita_totale
FROM Vendite
GROUP BY prodotto
ORDER BY quantita_totale ASC
LIMIT 3;

SELECT prodotto, SUM(quantita) AS quantita_totale
FROM Vendite
GROUP BY prodotto
ORDER BY quantita_totale ASC
LIMIT 3;