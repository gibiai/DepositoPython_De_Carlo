# Gestore file per modifica e creazione di prenotazione (su file mutilpli)

import random # libreria per generare numeri casuali
import os # libreria per gestire file e cartelle

class Utente: # classe per rappresentare un utente
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_utente = random.randint(1000, 9999) # ID casuale tra 1000 e 9999

    def __str__(self): # metodo per stampare l'utente come stringa
        return f"Utente: {self.nome} {self.cognome} ({self.email}) - ID: {self.id_utente}"


def crea_prenotazione(utente): # crea una nuova prenotazione su file dedicato
    print("\n--- NUOVA PRENOTAZIONE ---")
    id_prenotazione = random.randint(100, 999) # ID prenotazione casuale
    servizio = input("Servizio (es. Hotel, Ristorante): ")
    data = input("Data prenotazione (es. 10/05/2026): ")
    note = input("Note aggiuntive: ")

    nome_file = f"prenotazione_{id_prenotazione}.txt" # file dedicato per ogni prenotazione

    prenotazione = f"PRENOTAZIONE #{id_prenotazione}\n{utente}\nServizio: {servizio}\nData: {data}\nNote: {note}\nStato: ATTIVA\n"

    with open(nome_file, "w") as file: # "w" crea un nuovo file
        file.write(prenotazione)
    print(f"Prenotazione #{id_prenotazione} creata!")


def modifica_prenotazione(): # modifica una prenotazione esistente cercandola per ID
    id_cerca = input("ID prenotazione da modificare: ")
    nome_file = f"prenotazione_{id_cerca}.txt" # costruisce il nome del file

    try: # controllo flusso degli errori / controlla anomalie e gestisce errori tempo esecuzione
        with open(nome_file, "r") as file: # "r" legge il file
            contenuto = file.read()
            print("\nPrenotazione attuale:")
            print(contenuto)

        print("\nCosa vuoi modificare?")
        print("1 - Data")
        print("2 - Note")
        print("3 - Stato")

        scelta = input("Scelta: ")
        match scelta:
            case "1":
                nuova_data = input("Nuova data: ")
                vecchia_data = [line for line in contenuto.split("\n") if "Data:" in line][0] # trova la riga con la data
                contenuto = contenuto.replace(vecchia_data, f"Data: {nuova_data}") # sostituisce la data
            case "2":
                nuove_note = input("Nuove note: ")
                vecchie_note = [line for line in contenuto.split("\n") if "Note:" in line][0] # trova la riga con le note
                contenuto = contenuto.replace(vecchie_note, f"Note: {nuove_note}") # sostituisce le note
            case "3":
                nuovo_stato = input("Nuovo stato (es. ANNULLATA): ")
                vecchio_stato = [line for line in contenuto.split("\n") if "Stato:" in line][0] # trova la riga con lo stato
                contenuto = contenuto.replace(vecchio_stato, f"Stato: {nuovo_stato}") # sostituisce lo stato
            case _:
                print("Scelta non valida!")
                return

        with open(nome_file, "w") as file: # "w" sovrascrive il file con le modifiche
            file.write(contenuto)
        print("Prenotazione modificata!")

    except FileNotFoundError: # se il file non esiste
        print(f"Prenotazione #{id_cerca} non trovata!")


def leggi_prenotazioni(): # legge e stampa tutte le prenotazioni esistenti
    trovate = False # flag per sapere se ci sono prenotazioni
    for file_name in os.listdir("."): # scorre tutti i file nella cartella corrente
        if file_name.startswith("prenotazione_"): # filtra solo i file prenotazione
            with open(file_name, "r") as file: # "r" legge il file
                print("\n" + file.read())
            trovate = True
    if not trovate: # se non ha trovato nessun file
        print("Nessuna prenotazione trovata.")


def menu(utente): # menu principale ripetibile
    while True: # ciclo si ripete finché vero
        print("\n--- MENU ---")
        print("1 - Crea prenotazione")
        print("2 - Modifica prenotazione")
        print("3 - Leggi prenotazioni")
        print("4 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                crea_prenotazione(utente)
            case "2":
                modifica_prenotazione()
            case "3":
                leggi_prenotazioni()
            case "4":
                print("Arrivederci!")
                break # esce dal while
            case _:
                print("Scelta non valida!")


# avvio del programma
print("Inserisci i tuoi dati:")
nome = input("Nome: ")
cognome = input("Cognome: ")
email = input("Email: ")
utente = Utente(nome, cognome, email) # crea oggetto utente con i dati inseriti
menu(utente) # avvia il menu