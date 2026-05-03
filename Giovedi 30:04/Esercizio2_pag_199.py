# Gestore file per visita medica con accettazione postuma

import random # libreria per generare numeri casuali
from datetime import date # libreria per la data odierna

class Utente: # classe per rappresentare un paziente
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_paziente = random.randint(1000, 9999) # ID casuale tra 1000 e 9999

    def __str__(self): # metodo per stampare l'utente come stringa
        return f"Paziente: {self.nome} {self.cognome} ({self.email}) - ID: {self.id_paziente}"


def crea_visita(utente): # crea e salva una visita medica in attesa di accettazione
    print("\n--- NUOVA VISITA MEDICA ---")
    medico = input("Nome medico: ")
    specializzazione = input("Specializzazione: ")
    data = input("Data visita (es. 10/05/2026): ")
    note = input("Note: ")

    visita = f"VISITA MEDICA - IN ATTESA\n{utente}\nMedico: {medico} ({specializzazione})\nData: {data}\nNote: {note}\nStato: IN ATTESA\n\n"

    with open("visite.txt", "a") as file: # "a" aggiunge senza sovrascrivere
        file.write(visita)
    print("Visita salvata - in attesa di accettazione!")


def accetta_visita(): # accetta una visita cercandola per ID paziente
    try: # controllo flusso degli errori / controlla anomalie e gestisce errori tempo esecuzione
        with open("visite.txt", "r") as file: # "r" legge il file
            contenuto = file.read()

        id_cerca = input("Inserisci ID paziente da accettare: ")

        if id_cerca in contenuto: # controlla se l'ID esiste nel file
            contenuto = contenuto.replace(
                f"ID: {id_cerca}\n", f"ID: {id_cerca}\n" # riga invariata
            )
            contenuto = contenuto.replace(
                "Stato: IN ATTESA", "Stato: ACCETTATA" # cambia lo stato
            )
            with open("visite.txt", "w") as file: # "w" sovrascrive il file aggiornato
                file.write(contenuto)
            print("Visita accettata!")
        else:
            print("ID paziente non trovato!")

    except FileNotFoundError: # se il file non esiste
        print("Nessuna visita trovata.")


def leggi_visite(): # legge e stampa tutte le visite salvate
    try:
        with open("visite.txt", "r") as file: # "r" legge il file
            contenuto = file.read()
            print("\n" + contenuto)
    except FileNotFoundError: # se il file non esiste
        print("Nessuna visita trovata.")


def menu(utente): # menu principale ripetibile
    while True: # ciclo si ripete finché vero
        print("\n--- MENU ---")
        print("1 - Crea visita medica")
        print("2 - Accetta visita")
        print("3 - Leggi visite")
        print("4 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                crea_visita(utente)
            case "2":
                accetta_visita()
            case "3":
                leggi_visite()
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