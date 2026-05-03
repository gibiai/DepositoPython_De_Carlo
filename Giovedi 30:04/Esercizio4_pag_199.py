# Gestore file per Creazione di aule (Lista di studenti e professori)

import random # libreria per generare numeri casuali
import os # libreria per gestire file e cartelle

class Utente: # classe per rappresentare un utente generico
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_utente = random.randint(1000, 9999) # ID casuale tra 1000 e 9999

    def __str__(self): # metodo per stampare l'utente come stringa
        return f"{self.nome} {self.cognome} ({self.email}) - ID: {self.id_utente}"


def crea_aula(): # crea un nuovo file aula con nome e professore
    print("\n--- CREA NUOVA AULA ---")
    nome_aula = input("Nome aula (es. Aula1): ")
    professore = input("Nome professore: ")
    materia = input("Materia: ")

    nome_file = f"aula_{nome_aula}.txt" # file dedicato per ogni aula

    if os.path.exists(nome_file): # controlla se l'aula esiste già
        print(f"Aula {nome_aula} esiste già!")
        return

    contenuto = f"AULA: {nome_aula}\nProfessore: {professore}\nMateria: {materia}\nSTUDENTI:\n"

    with open(nome_file, "w") as file: # "w" crea il file
        file.write(contenuto)
    print(f"Aula {nome_aula} creata!")


def aggiungi_studente(utente): # aggiunge uno studente a un'aula esistente
    print("\n--- AGGIUNGI STUDENTE ---")
    nome_aula = input("Nome aula: ")
    nome_file = f"aula_{nome_aula}.txt" # costruisce il nome del file

    try: # controllo flusso degli errori / controlla anomalie e gestisce errori tempo esecuzione
        with open(nome_file, "a") as file: # "a" aggiunge senza sovrascrivere
            file.write(f"- {utente}\n") # aggiunge l'utente come studente
        print(f"Studente aggiunto all'aula {nome_aula}!")

    except FileNotFoundError: # se il file non esiste
        print(f"Aula {nome_aula} non trovata!")


def leggi_aula(): # legge e stampa il contenuto di un'aula
    nome_aula = input("Nome aula da leggere: ")
    nome_file = f"aula_{nome_aula}.txt"

    try:
        with open(nome_file, "r") as file: # "r" legge il file
            print("\n" + file.read())
    except FileNotFoundError: # se il file non esiste
        print(f"Aula {nome_aula} non trovata!")


def leggi_tutte_aule(): # legge e stampa tutte le aule esistenti
    trovate = False # flag per sapere se ci sono aule
    for nome_file in os.listdir("."): # scorre tutti i file nella cartella
        if nome_file.startswith("aula_"): # filtra solo i file aula
            with open(nome_file, "r") as file: # "r" legge il file
                print("\n" + file.read())
            trovate = True
    if not trovate: # se non ha trovato nessun file
        print("Nessuna aula trovata.")


def menu(utente): # menu principale ripetibile
    while True: # ciclo si ripete finché vero
        print("\n--- MENU ---")
        print("1 - Crea aula")
        print("2 - Aggiungi studente all'aula")
        print("3 - Leggi aula")
        print("4 - Leggi tutte le aule")
        print("5 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                crea_aula()
            case "2":
                aggiungi_studente(utente)
            case "3":
                leggi_aula()
            case "4":
                leggi_tutte_aule()
            case "5":
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