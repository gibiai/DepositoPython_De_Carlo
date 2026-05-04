# gestione_file.py - Modulo gestione file e credenziali
import csv # libreria per gestione file csv
from studente import Studente # importo classe Studente

def registra_utente(nome, password): # controlla duplicati e salva nuovo utente
    try:
        with open("credenziali.txt", "r") as file: # "r" legge il file
            righe = file.readlines() # legge tutte le righe

        def controlla(riga): # funzione che controlla se il nome esiste già
            return riga.split(",")[0] == nome # confronta il nome sulla prima colonna

        if list(filter(controlla, righe)): # se filter trova qualcosa - utente esiste
            return False # registrazione bloccata - utente già esistente

    except FileNotFoundError: # se il file non esiste ancora
        pass # continua e crea il file

    with open("credenziali.txt", "a") as file: # "a" aggiunge senza sovrascrivere
        file.write(f"{nome},{password}\n") # salva nome e password separati da virgola
    return True # registrazione riuscita

def login_utente(nome, password): # verifica credenziali su file
    try:
        with open("credenziali.txt", "r") as file: # "r" legge il file
            righe = file.readlines() # legge tutte le righe

        def controlla(riga): # funzione che controlla nome e password
            dati = riga.strip().split(",") # strip() rimuove \n, split divide per virgola
            return len(dati) == 2 and dati[0] == nome and dati[1] == password # controlla entrambi

        return len(list(filter(controlla, righe))) > 0 # True se trova corrispondenza

    except FileNotFoundError: # se il file non esiste
        return False # nessun utente registrato

def salva_studenti(lista_studenti): # salva lista studenti su file csv
    with open("studenti.csv", "w", newline="") as file: # "w" sovrascrive il file
        writer = csv.writer(file) # crea writer csv
        for studente in lista_studenti: # scorre tutti gli studenti
            writer.writerow([studente.nome, studente.corso]) # scrive riga csv

def carica_studenti(): # carica studenti dal csv e li converte in oggetti
    lista_studenti = [] # lista vuota
    try:
        with open("studenti.csv", "r") as file: # "r" legge il file
            reader = csv.reader(file) # crea reader csv
            for riga in reader: # scorre ogni riga
                if len(riga) == 2: # controlla che la riga sia valida
                    studente = Studente(riga[0], riga[1]) # crea oggetto Studente da csv
                    lista_studenti.append(studente) # aggiunge alla lista
    except FileNotFoundError: # se il file non esiste
        pass # lista rimane vuota
    return lista_studenti # restituisce la lista
