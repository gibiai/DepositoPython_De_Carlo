-- SETUP
USE gestioneordini;

-- ESERCIZIO 1 - INNER JOIN
-- mostra solo i clienti che hanno almeno un ordine
SELECT Clienti.nome, Ordini.data_ordine, Ordini.importo
FROM Clienti
INNER JOIN Ordini 
ON Clienti.id = Ordini.id_cliente;

-- ESERCIZIO 2 - LEFT JOIN
-- mostra tutti i clienti, anche quelli senza ordini
INSERT INTO Clienti (nome, città) VALUES ('Test Cliente', 'Roma');

SELECT Clienti.nome, Ordini.data_ordine, Ordini.importo
FROM Clienti
LEFT JOIN Ordini 
ON Clienti.id = Ordini.id_cliente;

-- ESERCIZIO 3 - RIGHT JOIN
-- mostra tutti gli ordini, anche quelli senza cliente

SELECT Clienti.nome, Ordini.data_ordine, Ordini.importo
FROM Clienti
RIGHT JOIN Ordini 
ON Clienti.id = Ordini.id_cliente;





