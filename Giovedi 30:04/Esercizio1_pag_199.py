# Gestore file Ricevuta di acquisto e ricevuta di ordine(su singolo file)

import random # libreria per generare numeri casuali

class Utente: # classe per rappresentare un utente
    def __init__(self, nome, cognome, email):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.id_cliente = random.randint(1000, 9999) # ID casuale tra 1000 e 9999

    def __str__(self): # metodo per stampare l'utente come stringa
        return f"Cliente: {self.nome} {self.cognome} ({self.email}) - ID: {self.id_cliente}"


def crea_ricevuta_acquisto(utente): # crea e salva una ricevuta di acquisto
    print("\n--- RICEVUTA DI ACQUISTO ---")
    prodotto = input("Nome prodotto: ")
    prezzo = float(input("Prezzo (€): "))

    ricevuta = f"RICEVUTA DI ACQUISTO\n{utente}\nProdotto: {prodotto}\nTotale: €{prezzo:.2f}\n\n"

    with open("ricevute.txt", "a") as file: # "a" aggiunge senza sovrascrivere
        file.write(ricevuta)
    print("Ricevuta di acquisto salvata!")


def crea_ricevuta_ordine(utente): # crea e salva una ricevuta di ordine
    print("\n--- RICEVUTA DI ORDINE ---")
    prodotto = input("Nome prodotto: ")
    prezzo = float(input("Prezzo (€): "))
    consegna = input("Data consegna (es. 10/05/2026): ")

    ricevuta = f"RICEVUTA DI ORDINE\n{utente}\nProdotto: {prodotto}\nTotale: €{prezzo:.2f}\nConsegna: {consegna}\n\n"

    with open("ricevute.txt", "a") as file: # "a" aggiunge senza sovrascrivere
        file.write(ricevuta)
    print("Ricevuta di ordine salvata!")


def leggi_ricevute(): # legge e stampa tutte le ricevute salvate
    try: # prova ad aprire il file / controllo flusso degli errori / controlla anomalie e gestisce errori tempo esecuzione
        with open("ricevute.txt", "r") as file: # "r" legge il file
            contenuto = file.read()
            print("\n" + contenuto)
    except FileNotFoundError: # se il file non esiste
        print("Nessuna ricevuta trovata.")


def menu(utente): # menu principale ripetibile
    while True: # ciclo si ripete finché vero
        print("\n--- MENU ---")
        print("1 - Crea ricevuta di acquisto")
        print("2 - Crea ricevuta di ordine")
        print("3 - Leggi ricevute")
        print("4 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1":
                crea_ricevuta_acquisto(utente)
            case "2":
                crea_ricevuta_ordine(utente)
            case "3":
                leggi_ricevute()
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