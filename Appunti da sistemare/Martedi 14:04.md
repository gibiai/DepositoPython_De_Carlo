int davanti parentesi è conversione, perchè eta può diventare numero da stringa

sempre definire le variabili prima di usarle
null tipo vuoto se non tipizzato

possiamo stampare ma anche operazioni di calcolo
funzionale quindi funzioni
incapsulamento contenere funzioni reali senza problemi

print(1 + 2) comprova tutte le regole fondamentali

COMMENTI NON ALLUNGANO O RALLENTANO
nno vengono letti dalla macchina
cancelletto metodo classico poi tre virgolette inizio e fine
visual studio code permette col tasto destro
commento riga singola spiegazioni
commento multiriga serve a bloccare un pezzo di codice (per cambiarlo eventualmente)


variabili e i loro tipi
poi liste (mettere dentro variabili)
infine if 

3 argomenti di oggi

domani controllo del flusso


variabile spazio di memoria definito da un nome e da un tipo. che fa da contenitore per un valore variabile per l’appunto

due regole qui
i nomi devono essere sempre descrittivi e se possibile brevi

meglio scrivere per lungo variabile 
sempre seguire queste regole:
mai spazi
solo lettere numeri e underscore (no “!” per esempio)
devono iniziare con una LETTERE MINUSCOLA
neance underscore perchè indica incapsulamento

LETTERE MAIUSCOLE solo classi e oggetti
oggeti maiuscola _ nome

pagina 20 sono le regole variabili

vengono assegnate con = che indica assegnazione
uno dei più complicati come indicatori
interno del contesto dell varibili assegnareun valore è molto complicato

varibili sempre nomi e tipo
tipi di dati:
in tutto l’oop esistono due macrotipologie di dato: 
Tipi basilari - già definiti nel linguaggio piu’ regole ma semplici
tipi non basilari - siamo noi a definirli nel linguaggio

basilari: int - float - str - char - boolean
str* sono un tipo speciale
definendo 0 per la logica è intero ma è inteso come mancaza di valore (falso) quindi per la macchina è un booleano

float numeri con la virgola, ma si scrive con il punto . 
tupla ( 3, 15)
1% diverso con le parentesi sono le tuple

121 unico 
ciao invece rappresenta 4 valori, 4 lettere
le str sono composte di char 
char unità basilare delle stringhe 
char = ‘A’ 
perchè esistono ancora i char? per via della tastiera
e sono in disuso

str speciali per due motivi
1 non sono un unico valore ma lo rappresentano formate da singoli char e quindi ciclabili
2 hanno i metodi propri
tipo print(s.upper()) 

sempre racchiusa tra “” apice singolo alcune caratteristiche e linguaggi di programmazione
inoltre la str modifica il funzionamento di alcune caratteristiche
ad esempio il + che somma o concatena
si occupa di unire due str

s = “Python”

str non sono oggetti perchè non hanno il costruttore
sono esattamente un tipo basilare? Risposta no, cioè si ma speciale
questi metodi sono: 
upper - lower - split - replace
len è un metodo che lavoro anche sulle str
è una funzione
si capisce dalla mancanza del . len non è subordinato

“ Esplorazione dei metodi “
perchè oggi 50 metodi, ma numpy sono presenti 12222 metodi
al lavoro ne servono non tantissimi ma può servire magari qualcuno di più
il trucco non è conoscerli ma cercare di analizzare quando si ha bisogno
ultime slides sono esplorazione dei metodi

per diventare bravo in Python conviene farsi le proprie analisi

char serve forse nel decryptaggio dei dati

booleani, il tipo più importante di tutti
base della programmazione 
true or false
1 or 0

alla base di tutte le condizione e logiche booleane

x = true y = false
sono case sensitive quindi maiuscola iniziale sempre

usati per combinare condizioni o capire valori
operatori boolean 
 
= = uguaglianza/identico a 
!= non uguale/ diverso da 
< minore di > maggiore di
<= minore o uguale a >= maggiore o uguale a

IF altro file esempio condizioni
letti anche da linguaggi a basso livello ma in sintassi diversa

javaffim javascript in napoletano

si possono fare più domande assieme con operatori logici
e appartengono alla logica stessa del codice stessa
aiutano i booleani a dimostrare la logica e la matematica 
rappresentazione astratta dentro il sistema macchina

and true se entrambe vere
or true se una è vera
not restituisce il valore contrario di ciò che segue

logica umana dentro la macchina

Collezioni o aggregazione in Python. ma si chiamano collezioni

collezioni insieme di valori con unico nome
4 caratteristiche:
definizione (definite in parentesi QUADRE)
tipo (ovviamente tipo list)
uguaglianza (sono eteerogenee - contenere diversi valori di tipi)
modificabilità (sono ordinate e modificate)
sono il tipo più utilizzato in python

saranno le mie migliore amiche

tipi
numer = [1, 2, 3, 4, 5]
print(numeri[0]) # Output 1
print(numeri[2]) # Output 3

lista parte anche lei a contare da zero
lista è struttura dati quindi non basilari, collezioni

LE liste sono modificabili
numeri[2] = 10
e hanno anche i metodi
alcuni basilari ovver che servono a farla funzionare come appen
numeri.appen(6) aggiunge
numeri.insert(2, 10) inserisce alla posizione specifica
numeri.remove(4) rimuove ovviamente
numeri.sort() organizza tramite una logica applicativa

controllo del flusso
IF adesso, da mettere nel nuovo file

python ha due famiglie di controlli del flusso
i cicli e le condizioni
la funzione è un esempio di astrazione non controllo del flusso
condizioni if e match
poi la seconda famiglia dei cicli con while e for

if se questa condizione si verifica
con i cicli: se accade questo o non accade questo, ripeti

le condizioni eseguono un blocco solo se
i cicli ripetono un blocco fino a che
if quanti vuoi
else solo uno per blocco e sempre alla fine
in mezzo posso avere infiniti elif
elif sono condizioni secondarie

naturalmnte bisogna avere una logica
i blocchi tra di loro devono essere autoescludenti
if sempre con condizione
infiniti elif con condizione
else sarebbe l’altrimenti. quindi non ha condizione e non è obbligatorio
if annidato, sarebbe if dentro un if

if ovviamente non ha metodi non essendo un elemento
perchè è una parte funzionale che si occupa di eseguire un’operazione

if x:  sarebbe chiedere tru

i blocchi di codice possono essere collassati
proprietarietà

il primo input è sempre stringa quindi nel caso successivo dovrei castare int per esempio prima delle parentesi di intput
parola = input(“dimmi il nome”)

parola == “mirko”
numero > 10

per fare questa cosa serve una lista aggiungere modificare o eliminare

slide 68 per studiare pomeriggio

