-- 1) INSERT INTO
INSERT INTO Libri VALUES (1, 'Il Nome della Rosa', 'Umberto Eco', 'Storico', 12.99, 1980);
INSERT INTO Libri VALUES (2, 'Harry Potter', 'J.K. Rowling', 'Fantasy', 15.99, 1997);
INSERT INTO Libri VALUES (3, '1984', 'George Orwell', 'Distopico', 9.99, 1949);
INSERT INTO Libri VALUES (4, 'It', 'Stephen King', 'Horror', 14.99, 1986);
INSERT INTO Libri VALUES (5, 'Dune', 'Frank Herbert', 'Fantascienza', 11.99, 1965);
INSERT INTO Libri VALUES (6, 'Sapiens', 'Yuval Harari', 'Saggistica', 13.99, 2011);


-- 2) GROUP BY
SELECT genere, COUNT(*), AVG(prezzo)
FROM Libri
GROUP BY genere
ORDER BY genere ASC;


-- 3) ORDER BY
SELECT *
FROM Libri
WHERE anno_pubblicazione > 2010
ORDER BY anno_pubblicazione DESC, prezzo ASC;