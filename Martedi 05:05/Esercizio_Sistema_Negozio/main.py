# main.py - Modulo principale - gestione menu e avvio
from cliente import Cliente # importo classe Cliente
from gestione_inventario import carica_inventario, salva_inventario, aggiungi_articolo, rimuovi_articolo, aggiorna_articolo, stampa_inventario # importo funzioni inventario
from amministrazione import rapporto_vendite # importo funzione rapporto


def menu_cliente(cliente): # menu per cliente loggato 
    while True: # ciclo ripetibile
        print(f"\n--- MENU CLIENTE ({cliente.nome} {cliente.cognome}) ---")
        print("1 - Visualizza inventario")
        print("2 - Acquista articolo")
        print("3 - Visualizza miei acquisti")
        print("4 - Esci")

        scelta = input("Scelta: ")
        inventario = carica_inventario() # carica inventario dal csv

        match scelta:
            case "1": # visualizza articoli disponibili
                stampa_inventario(inventario)

            case "2": # acquista articolo dall'inventario
                stampa_inventario(inventario) # mostra cosa è disponibile
                nome_cerca = input("Nome articolo da acquistare: ")

                def controlla_nome(articolo): # funzione che controlla se il nome corrisponde
                    return articolo.nome.lower() == nome_cerca.lower()

                trovati = list(filter(controlla_nome, inventario)) # filtra inventario

                if len(trovati) == 0: # se non ha trovato nessuno
                    print("Articolo non trovato!")
                else:
                    articolo = trovati[0] # prende il primo trovato
                    if articolo.quantita == 0: # controlla disponibilità
                        print("Articolo esaurito!")
                    else:
                        articolo.quantita -= 1 # scala quantità di 1
                        cliente.aggiungi_acquisto(articolo.nome, articolo.prezzo) # aggiunge acquisto
                        salva_inventario(inventario) # salva inventario aggiornato
                        print(f"Acquistato {articolo.nome} per {articolo.prezzo:.2f}€!")

            case "3": # visualizza acquisti del cliente
                if len(cliente.acquisti) == 0: # controlla che ci siano acquisti
                    print("Nessun acquisto effettuato.")
                else:
                    print("\n--- I TUOI ACQUISTI ---")
                    for acquisto in cliente.acquisti: # scorre lista dizionari
                        print(f"- {acquisto['articolo']}: {acquisto['prezzo']:.2f}€") # legge chiavi dizionario

            case "4": # esce dal menu cliente e salva
                cliente.salva() # salva tutto prima di uscire
                break

            case _:
                print("Scelta non valida!")


def menu_admin(): # menu per amministratore - hardcodato
    while True: # ciclo ripetibile
        print("\n--- MENU ADMIN ---")
        print("1 - Visualizza inventario")
        print("2 - Aggiungi articolo")
        print("3 - Rimuovi articolo")
        print("4 - Aggiorna articolo")
        print("5 - Rapporto vendite")
        print("6 - Esci")

        scelta = input("Scelta: ")
        inventario = carica_inventario() # carica inventario dal csv

        match scelta:
            case "1":
                stampa_inventario(inventario)
            case "2":
                aggiungi_articolo(inventario)
                salva_inventario(inventario) # salva dopo modifica
            case "3":
                rimuovi_articolo(inventario)
                salva_inventario(inventario) # salva dopo modifica
            case "4":
                aggiorna_articolo(inventario)
                salva_inventario(inventario) # salva dopo modifica
            case "5":
                rapporto_vendite() # genera rapporto da file clienti
            case "6":
                break
            case _:
                print("Scelta non valida!")


def menu_principale(): # menu principale - accesso cliente o admin
    while True: # ciclo ripetibile
        print("\n--- BENVENUTO ---")
        print("1 - Accedi come cliente")
        print("2 - Accedi come admin")
        print("3 - Esci")

        scelta = input("Scelta: ")

        match scelta:
            case "1": # accesso cliente - inserisce nome e cognome
                nome = input("Nome: ")
                cognome = input("Cognome: ")
                cliente = Cliente(nome, cognome) # crea oggetto cliente
                menu_cliente(cliente) # apre menu cliente

            case "2": # accesso admin - password hardcodata
                password = input("Password admin: ")
                if password == "admin": # controlla password hardcodata
                    menu_admin() # apre menu admin
                else:
                    print("Password errata!")

            case "3":
                print("Arrivederci!")
                break

            case _:
                print("Scelta non valida!")


# avvio del programma
menu_principale() # avvia il menu principale