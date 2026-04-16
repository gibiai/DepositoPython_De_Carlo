Giovedi 15

Tuple uniche constanti di Python
insieme collezioni matematiche
pag 62 recap operatori

booleani basi programmazione
controlli del flusso invece base dei linguaggi moderni

ripetere cicli while e for

tuple hanno tipo tupla, definite tramite parentesi tonde
sono miste e non sono modificabili (modificabili solo quando create) e ordinate
unico tipo constante di Python
utili per creare riferimenti sempre uguali

possiamo impacchettarle - packing (senza mettere le parentesi), per non confonderle con le funzioni
possiamo anche fare unpacking tutto assieme - qui assegnamo valori a variabili (da rivedere questo)

insiemi tipo sets, strutture dati con parentesi graffe
sono misti (in realtà omogeenei) , modificabili, e non ordinati
sono specializzati in non avere duplicati
da lista a set da set a tupla e vice versa
il set serve a due cose
evitare i duplicati , che non vengono stampati, ma sono ancora presenti al suo interno
non ordinato perchè non li stampa nell’ordine in cui sono entrati
seconda capacità: accetta i metodi matematici degli insiemi
 
break continue pass - rientrano in esempi cicli mercoledi

break se viene letto dentro un ciclo, chiude un ciclo senza ricontrollare la condizione
break rompe anche boolean
il continue salta un giro (per esempio due operazioni su 3 a - b - c, in wip, con continue salta la ripetizione. Mirko lo usa nei menu) non chiude il ciclo ma salta solo un giro
pass invece non da errore in un ciclo di if per esempio. indica un work in progress per continuare a ciclare, passa oltre quella condizione per poi terminarla dopo
permette di andare ad avere degli elementi fermi che non hanno correlazione, senza che si rompano
utile per architetture complesse
sempre aggiungere un commento sul pass

FUNZIONI
primo passo funzionale, livello più alto, porta d accesso sistemi migliorativi sistema python
blocco di codice autonomi che eseguono codice, ma scritte da noi
dimostrano implicitamente l’astrazione
astrazione regola teorica e pratica
se scrivo funz e non richiamiamo non fa nulla (questa è astrazione: capacità creare codice che la macchina vede ma con cui non fa nulla fino a quando non è richiamata. capacità essenziale in un linguaggio ad alto livello)
SOLO QUANDO DECIDO IO

funzioni di due tipo: senza return o con il return , definite tramite parola chiave def - nome della funzione e parentesi tonde dove inseriamo i parametri (elementi necessari a far funzionare la funzione)
i : dopo le parentesi sono obbligatori
def saluta(nome) placeholder per valore che poi daremo
funzione può avere infinite righe

Alice è valore reale come argomento
si possono usare anche delle variabili come argomento

funzione due fasi: definizione parametri, richiamo con i valori anche detti argomenti
TUTTE LE FUNZIONI

potrebbero anche non esserci parametri

return riporta risultato alla righe dove è stato scritto
funzione raggiunge un return per volta
per averne di più devo condizionare il codice (importante questo)
funzioni con return printano di base
possiamo anche tipizzare i parametri
e posso anche dare un parametro di default “ defsaluta(nome:str, messaggio=“Ciao”):”
solitamente si fa con pgreco da mettere nella tupla

f nel print metodo più veloce per stampare f”{} serve per richiamare nome variabili all’interno del print
utile ma non accettato da tutti i sistemi tipo linux e server
per rischio compromissione dei dati 
value idleing dentro  - dati richiamati all’esterno dove non dovrebbero o non dovrebbero potere

con dat format incapsulato
decoratori e generatori

funzione generatori 
andra avanti x volte
è un return che ritorna li
questo è lo yield
riporta elementi uno alla volta per ciclo
generatori funzioni ripetitive

decoratori modificano una funzione senza scrivere altro codice dentro
senza modificare il comportamento
aggiungono funzionalita extra (logging, controllo degli accessi)
si applicano con simbolo @
wrapper sempre chiamato wrapper colui che crea contenitore per la nostra funzione, all interno scriviamo nuovo flusso 
return wrapper dopo
puo essere messo il decoratore sopra quante funzioni vogliamo
modificabile e trasportabile ovunque
se non facciamo return wrapper lui non riporta niente

slide 98 tutta la teoria da studiare

*args, **kwargs serve a definire parametri 
va bene per qualsiasi gruppo di parametri
molto utile per creare decoratori ripetitivi (argomenti con return)
va bene su qualsiasi tipo di decorazione
facciamo accettare a qualsiasi funzione tutti i parametri possibile
dentro il denominatore avere multipli parametri

esercizio con menu (match (x): case1: funzione1() case 2: funzione2() ecc ecc)
ogni singola parte fatta in una funzione
tutto il menu in un while true che si deve ripetere fino al no dell’utente
per esempio case _: break
nel caso si tenta decoratore al punto 8 (punto extra)

