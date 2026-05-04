# gestione_studenti.py - Modulo gestione lista studenti
from studente import Studente # importo classe Studente

def aggiungi_studente(lista_studenti): # crea oggetto Studente e lo aggiunge alla lista
    print("\n--- AGGIUNGI STUDENTE ---")
    nome = input("Nome studente: ")
    corso = input("Corso: ")
    nuovo_studente = Studente(nome, corso) # crea oggetto Studente
    lista_studenti.append(nuovo_studente) # aggiunge alla lista
    print(f"Studente {nome} aggiunto!")


def cerca_studente(lista_studenti, nome_cerca): # cerca studente per nome con filter
    def controlla_nome(studente): # funzione che controlla se il nome corrisponde
        return studente.nome.lower() == nome_cerca.lower() # confronta ignorando maiuscole

    risultati = list(filter(controlla_nome, lista_studenti)) # filtra la lista
    return risultati # restituisce lista di studenti trovati


def modifica_studente(lista_studenti): # cerca studente e lo modifica tramite setter
    print("\n--- MODIFICA STUDENTE ---")
    nome_cerca = input("Nome studente da modificare: ")
    risultati = cerca_studente(lista_studenti, nome_cerca) # riuso cerca_studente per trovarlo

    if len(risultati) == 0: # se non ha trovato nessuno
        print("Studente non trovato!")
        return

    studente = risultati[0] # prende il primo risultato trovato
    print(f"Trovato: {studente.descrivi()}") # stampa descrizione studente trovato
    print("1 - Nome")
    print("2 - Corso")
    scelta = input("Scelta: ")

    match scelta:
        case "1":
            studente.nome = input("Nuovo nome: ") # chiama setter nome
            print("Nome aggiornato!")
        case "2":
            studente.corso = input("Nuovo corso: ") # chiama setter corso
            print("Corso aggiornato!")
        case _:
            print("Scelta non valida!")
            return

    print("Studente modificato!")


def stampa_aula(lista_studenti): # stampa tutti gli studenti ordinati per corso
    print("\n--- AULA ---")
    if len(lista_studenti) == 0: # controlla che ci siano studenti
        print("Nessuno studente presente.")
        return

    def prendi_corso(studente): # funzione chiave per l'ordinamento
        return studente.corso # ordina per corso

    lista_ordinata = sorted(lista_studenti, key=prendi_corso) # ordina usando prendi_corso come criterio
    for studente in lista_ordinata: # scorre studenti ordinati
        print(studente.descrivi()) # stampa descrizione di ogni studente


def reset_aula(lista_studenti, admin): # reset completo aula - solo admin
    motivazione = input("Motivazione del reset: ") # chiede motivazione obbligatoria
    admin.reset(motivazione) # chiama metodo reset dell'admin

    with open("intervento_utente.txt", "a") as file: # "a" aggiunge senza sovrascrivere
        file.write(f"{admin.nome} - {motivazione}\n") # salva log dell'intervento

    lista_studenti.clear() # svuota completamente la lista
    print("Aula resettata!")