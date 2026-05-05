# Modulo gestione inventario con csv
import csv # libreria gestione csv
from articolo import Articolo # importo tutto da articolo

#deserializzazione
def carica_inventario(): # carica articoli dal csv e li converte in oggetti
    inventario = [] # lista vuota
    try: # gestione errori / eccezioni 
        with open("inventario.csv", "r") as file: # apre/chiude e con "r" legge il file
            reader = csv.reader(file) # crea un reader csv leggendo riga per riga
            next(reader) # salta la riga di intestazione (Nome, Prezzo, Quantitò)
            for riga in reader: # scorre ogni riga
                if len(riga) == 3: # controlla che la riga sia valida (ha i 3 dati)
                    articolo = Articolo(riga[0], float(riga[1]), int(riga[2])) # istanziazione oggetto Articolo con casting dati presi dal file                  
                    inventario.append(articolo) # aggiunge alla lista
    except FileNotFoundError: # se il file non esiste
        pass # inventario rimane vuoto
    return inventario # restituisce inventario

#serializzazione
def salva_inventario(inventario): # salva lista articoli su csv "aggiornandosi" ogni volta
    with open("inventario.csv", "w", newline="") as file: # apre/chiude e con "w" sovrascrive tutto il file evitando doppie spaziature grazie a newline
        writer = csv.writer(file) # crea un writer csv
        writer.writerow(["nome", "prezzo", "quantita"]) # scrive intestazione
        for articolo in inventario: # scorre tutti gli articoli
            writer.writerow([articolo.nome, articolo.prezzo, articolo.quantità]) # scrive riga csv

def aggiungi_articolo(inventario): # aggiunge nuovo articolo all'inventario con parametri inseriti
    print("\n--- AGGIUNGI ARTICOLO ---")
    nome = input("Nome articolo: ")
    prezzo = float(input("Prezzo: "))
    quantità = int(input("Quantità: "))
    inventario.append(Articolo(nome, prezzo, quantità)) # crea e aggiunge nuovo oggetto in lista
    print(f"Articolo {nome} aggiunto!")

def rimuovi_articolo(inventario): # rimuove articolo cercandolo per nome con filter
    print("\n--- RIMUOVI ARTICOLO ---")
    nome_cerca = input("Nome articolo da rimuovere: ")

    def controlla_nome(articolo): # funzione annidata che controlla se il nome corrisponde
        return articolo.nome.lower() == nome_cerca.lower() # confronta se corrisponde ignorando maiuscole

    trovati = list(filter(controlla_nome, inventario)) # filtra la lista per nome

    if len(trovati) == 0: # se non ha trovato nessuno
        print("Articolo non trovato!")
        return

    inventario.remove(trovati[0]) # rimuove il primo trovato dalla lista originale
    print(f"Articolo {nome_cerca} rimosso!")

def aggiorna_articolo(inventario): # aggiorna prezzo o quantità di un articolo
    print("\n--- AGGIORNA ARTICOLO ---")
    nome_cerca = input("Nome articolo da aggiornare: ")

    def controlla_nome(articolo): # funzione annidata che controlla se il nome corrisponde
        return articolo.nome.lower() == nome_cerca.lower()

    trovati = list(filter(controlla_nome, inventario)) # filtra la lista per nome

    if len(trovati) == 0: # se non ha trovato nessuno
        print("Articolo non trovato!")
        return

    articolo = trovati[0] # prende il primo trovato
    print(f"Trovato: {articolo.descrivi()}")
    print("1 - Aggiorna prezzo")
    print("2 - Aggiorna quantità")
    scelta = input("Scelta: ")

    match scelta:
        case "1":
            articolo.prezzo = float(input("Nuovo prezzo: ")) # chiama setter prezzo
            print("Prezzo aggiornato!")
        case "2":
            articolo.quantita = int(input("Nuova quantità: ")) # chiama setter quantità
            print("Quantità aggiornata!")
        case _:
            print("Scelta non valida!")

def stampa_inventario(inventario): # stampa tutti gli articoli disponibili
    print("\n--- INVENTARIO ---")
    if len(inventario) == 0: # controlla che ci siano articoli
        print("Inventario vuoto.")
        return
    for articolo in inventario: # scorre tutti gli articoli
        print(articolo.descrivi()) # stampa descrizione di ogni articolo