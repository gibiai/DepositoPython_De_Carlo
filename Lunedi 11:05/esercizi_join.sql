# Esercizio 1 - troverà tutti casi dell'utente e dell'ordine effettuato
SELECT clienti2.nome, ordini.data_ordine, ordini.importo
FROM clienti2
INNER JOIN ordini ON clienti2.id = ordini.id_cliente
ORDER BY clienti2.nome ASC;

# Esercizio 2 - lista di clienti anche se non hanno fatto ordini
SELECT clienti2.nome, ordini.data_ordine, ordini.importo
FROM clienti2
LEFT JOIN ordini ON clienti2.id = ordini.id_cliente
ORDER BY ordini.data_ordine ASC;

# Esercizio 3 - 
SELECT clienti2.nome, ordini.data_ordine, ordini.importo
FROM clienti2
RIGHT JOIN ordini ON clienti2.id = ordini.id_cliente
ORDER BY clienti2.nome ASC
 