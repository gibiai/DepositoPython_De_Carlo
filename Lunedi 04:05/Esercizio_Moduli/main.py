from giorno import Giorno # importo classe Giorno
from inserimento import inserisci_vendite # importo funzione inserimento
from analisi import calcola_totale, calcola_media, giorni_sopra_media # importo funzioni analisi
from gestione_file import salva_risultati, leggi_risultati # importo funzioni file

def stampa_risultati(giorni): 
    if len(giorni) == 0: # check se assenza dati
        print("Nessun dato presente.")
        return
    
    print("\n" + "=" * 40) # cornice - separatore visivo titolo
    print("RIEPILOGO VENDITE")
    print("=" * 40)
    
    for giorno in giorni: # stampa descrizione di ogni giorni
        print(giorno.descrizione()) # stampa ogni giorno eseguendo il metodo di istanza
    
    # assegnazione di valori a variabili    
    totale = calcola_totale(giorni) # calcola totale generale
    media = calcola_media(giorni) # calcola media generale
    sopra = giorni_sopra_media(giorni) # trova giorni sopra media
    
    print(f"\nTotale generale: {totale:.2f}€")
    print(f"Media generale: {media:.2f}€")

    if len(sopra) > 0: # stampa ogni giorno sopra media SE esistono
        print("\nGiorni sopra la media:")
        for giorno in sopra:
            print(f" - {giorno.descrizione()}")
    else:
        print("\nNessun giorno sopra la media")
        
    return totale, media, sopra # restituisce tutti i valori per salvarli

def menu(): # menu principale ripetibile
    giorni = [] # lista vuota per i giorni finchè programma aperto
    numero_giorno = 1 # contatore giorni - segnaposto dinamico

    while True: # ciclo si ripete finché vero
        print("\n--- MENU ---")
        print("1 - Inserisci vendite del giorno")
        print("2 - Analizza e stampa risultati")
        print("3 - Salva risultati su file")
        print("4 - Leggi risultati salvati")
        print("5 - Esci")

        scelta = input("Scelta: ")
        
        match scelta:
            case "1": # inserisce le vendite di un nuovo giorno
                data = input(f"Data del giorno {numero_giorno} (es. 04/05/2026): ")
                vendite = inserisci_vendite(data) # chiama inserimento con gestione errori
                giorno = Giorno(data, vendite) # crea oggetto Giorno
                giorni.append(giorno) # e lo aggiunge alla lista
                numero_giorno += 1 # incrementa contatore
                print(f"Giorno {data} aggiunto!") # stampa conferma

            case "2": # analizza e stampa i risultati - aggiornandoli
                risultati = stampa_risultati(giorni)
            
            case "3": # salva i risultati su file
                if len(giorni) == 0: # controlla che ci siano dati
                    print("Nessun dato da salvare!")
                else:
                    totale = calcola_totale(giorni)
                    media = calcola_media(giorni)
                    sopra = giorni_sopra_media(giorni)
                    salva_risultati(giorni, totale, media, sopra)

            case "4": # legge i risultati salvati
                leggi_risultati()

            case "5": # esce dal programma
                print("Arrivederci!")
                break # esce dal while e spegne il programma

            case _:
                print("Scelta non valida!")


# avvio del programma
menu() # avvia il menu