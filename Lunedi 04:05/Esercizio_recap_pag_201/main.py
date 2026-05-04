# main.py - Modulo principale - gestione menu e avvio
from utente import StudenteUtente, Admin # importo classi utente e admin
from gestione_studenti import aggiungi_studente, modifica_studente, cerca_studente, stampa_aula, reset_aula # importo funzioni studenti
from gestione_file import registra_utente, login_utente, salva_studenti, carica_studenti # importo funzioni file


def menu_studente(utente): # menu per utente normale - accessibile dopo login
    while True: # ciclo ripetibile
        print(f"\n--- MENU STUDENTI ({utente.nome}) ---")
        print("1 - Aggiungi studente")
        print("2 - Modifica studente")
        print("3 - Cerca studente")
        print("4 - Stampa aula")
        print("5 - Esci")

        scelta = input("Scelta: ")
        lista_studenti = carica_studenti() # carica sempre dal file prima di ogni operazione

        match scelta:
            case "1":
                aggiungi_studente(lista_studenti)
            case "2":
                modifica_studente(lista_studenti)
            case "3":
                nome = input("Nome da cercare: ")
                risultati = cerca_studente(lista_studenti, nome) # cerca con filter
                if len(risultati) == 0: # se non ha trovato nessuno
                    print("Studente non trovato!")
                for studente in risultati: # stampa ogni risultato trovato
                    print(studente.descrivi())
            case "4":
                stampa_aula(lista_studenti)
            case "5":
                break # esce dal while
            case _:
                print("Scelta non valida!")
                continue # salta salva_studenti se scelta non valida

        salva_studenti(lista_studenti) # salva sempre dopo ogni operazione


def menu_admin(admin): # menu per admin - ha poteri aggiuntivi
    while True: # ciclo ripetibile
        print(f"\n--- MENU ADMIN ({admin.nome}) ---")
        print("1 - Aggiungi studente")
        print("2 - Modifica studente")
        print("3 - Cerca studente")
        print("4 - Stampa aula")
        print("5 - Reset aula")
        print("6 - Esci")

        scelta = input("Scelta: ")
        lista_studenti = carica_studenti() # carica sempre dal file prima di ogni operazione

        match scelta:
            case "1":
                aggiungi_studente(lista_studenti)
            case "2":
                modifica_studente(lista_studenti)
            case "3":
                nome = input("Nome da cercare: ")
                risultati = cerca_studente(lista_studenti, nome) # cerca con filter
                if len(risultati) == 0: # se non ha trovato nessuno
                    print("Studente non trovato!")
                for studente in risultati: # stampa ogni risultato trovato
                    print(studente.descrivi())
            case "4":
                stampa_aula(lista_studenti)
            case "5":
                reset_aula(lista_studenti, admin) # reset - solo admin
            case "6":
                break # esce dal while
            case _:
                print("Scelta non valida!")
                continue # salta salva_studenti se scelta non valida

        salva_studenti(lista_studenti) # salva sempre dopo ogni operazione


def main(): # menu principale - registrazione e login
    while True: # ciclo ripetibile
        print("\n--- BENVENUTO ---")
        print("1 - Registrati")
        print("2 - Login")
        print("3 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1": # registrazione nuovo utente
                nome = input("Nome: ")
                password = input("Password: ")
                if registra_utente(nome, password): # salva se non esiste già
                    print("Registrazione completata!")
                else:
                    print("Utente già esistente!")
            case "2": # login utente o admin
                nome = input("Nome: ")
                password = input("Password: ")
                if nome == "admin" and password == "admin": # admin hardcodato
                    menu_admin(Admin()) # crea oggetto admin e apre menu admin
                elif login_utente(nome, password): # controlla credenziali su file
                    menu_studente(StudenteUtente(nome, password)) # crea utente e apre menu
                else:
                    print("Credenziali errate!")
            case "3":
                print("Arrivederci!")
                break # esce dal while
            case _:
                print("Scelta non valida!")


# avvio del programma
main() # avvia il menu principale