select * from world.country;

SELECT Continent FROM world.country;

select Region, Code, Name from world.country;

--- commento test

/*

Test multiriga
bla bla bla

*/

SELECT * FROM table_name;
--- dati restituiti vengono archiviati in un tabella temporanea, result-set non memorizzata
SELECT column1, column2
FROM table_name;

SELECT DISTINCT column1, column2 FROM table_name;
--- distinct restituisce array senza ripetizione
select count(distinct Continent) from world.country;
/* possiamo ad esempio sapere il numero di valori unici
usando il comando COUNT che conta i valori. */
--- esempio select distinct Continent from world.country
 
 --- clausola WHERE rende select più specifico
 SELECT column1, column2
 FROM table_name
 WHERE condizione;
 
 SELECT * FROM world.country
 WHERE Region='Antarctica';
 
 --- altro esempio con valore numerico
 SELECT * FROM world.country
 WHERE Population < 10000;
 /*
 Le operazioni che si possono fare come condizione sono:

= - uguale;

> - maggiore di;

< - minore di;

>= - maggiore uguale di;

<= - minore uguale di;

<> - non uguale(in alcune versione di SQL si scrive "!=", in altre ancora accetta entrambe le
scritture come in MySQL);


BETWEEN - tra un certo intervallo ("BETWEEN 0 and 10", valori compresi);

LIKE - cerca un pattern, ovvero cerca una eguaglianza parziale o totale specificando il pattern
fisso da trovare e le parti del dato variabili con un metacarattere come il "%" (esempio: "City
LIKE 's%' " per trovare i valori che iniziano con "s" o "S");

IN - per specificare più valori possibili (esempio "IN (0, 1000)");
 */
 
 --- NULL valore usato per dire che è vuoto
 
 select world.country
 where IndepYear is null; --- oppure is not null
 
 --- AND OR NOT
 
 SELECT column1, column2
FROM table_name
WHERE condition1 AND condition2 AND condition3;
--- where condition1 AND(condition2 or not condition3);

--- ORDER BY

SELECT column1, column2
FROM table_name
ORDER BY column1, column2 ASC;

--- esempio: ORDER BY Region, SurfaceArea DESC; qui viene prima ordinata la prima colonna e poi la seconda 

--- GROUP BY

SELECT Country, COUNT(CustomerID)
FROM Customers
GROUP BY Country;

select Region, Count(Region)
from world.country
group by Region
order by Region;

--- INSERT INTO

INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
INSERT INTO world.country(Code, Name, 2022)
values ('QBC', 

--- UPDATE

UPDATE world.country
SET Name = 'NuovoNome', Population = 48000
WHERE Code = 'QBC'

--- DELETE

DELETE FROM table_name 
WHERE condition;

--- JOIN
--- permette di creare una terza tabella unendone innumerevoli (a scelta)

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;
--- inner join è unire due insiemi
/* tipi di join:
(inner) join
left (outer) join
right (outer) join
full (outer) join 
*/











 
 