# entry point del programma — gestionale ristorante
# crea il gestionale, carica i dati dal CSV e avvia il menu principale
from gestionale import Gestionale
from file_manager import carica_csv, salva_csv, aggiungi_ordine, aggiungi_recensione, leggi_ordini, leggi_recensioni
from analisi import analizza_tutti, analizza_per_tipo, analizza_per_prezzo, analizza_file, analizza_disponibili
from visualizza import grafico_prezzi_per_tipo, grafico_distribuzione_tipi

# unica istanza del gestionale: tutte le funzioni lavorano su questo oggetto
# centralizza i dati per evitare duplicati in memoria
gestionale = Gestionale()


# sottomenu dedicato alla gestione degli ordini su file TXT
def menu_ordini():
    print("\n--- ORDINI ---")
    print("1. Visualizza ordini")
    print("2. Aggiungi ordine")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        leggi_ordini()                # legge e stampa ordini.txt
    elif scelta == "2":
        aggiungi_ordine()             # aggiunge una riga a ordini.txt
    elif scelta == "0":
        return                        # interrompe la funzione e torna al menu principale
    else:
        print("Scelta non valida.")


# sottomenu dedicato alle recensioni su file TXT
def menu_recensioni():
    print("\n--- RECENSIONI ---")
    print("1. Visualizza recensioni")
    print("2. Aggiungi recensione")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        leggi_recensioni()            # legge e stampa recensioni.txt
    elif scelta == "2":
        aggiungi_recensione()         # aggiunge una riga a recensioni.txt
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")


# sottomenu dedicato alle analisi statistiche e ai filtri
def menu_analisi():
    print("\n--- ANALISI ---")
    print("1. Analisi completa menu")
    print("2. Analisi per tipo di piatto")
    print("3. Analisi per fascia di prezzo")
    print("4. Analisi file (ordini/recensioni)")
    print("5. Analisi disponibilità")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        analizza_tutti(gestionale)              # calcola medie e piatti estremi
    elif scelta == "2":
        analizza_per_tipo(gestionale)           # usa filter() per categoria
    elif scelta == "3":
        analizza_per_prezzo(gestionale)         # usa filter() per range di prezzo
    elif scelta == "4":
        analizza_file(gestionale)               # visualizza storici esterni
    elif scelta == "5":
        analizza_disponibili(gestionale)        # usa filter() su booleano disponibile
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")


# sottomenu dedicato alla generazione di grafici con Matplotlib
def menu_visualizzazione():
    print("\n--- VISUALIZZAZIONE ---")
    print("1. Prezzo medio per tipo di piatto")
    print("2. Distribuzione piatti per tipo")
    print("0. Torna indietro")
    scelta = input("\nScelta: ").strip()

    if scelta == "1":
        grafico_prezzi_per_tipo(gestionale)       # genera grafico a barre
    elif scelta == "2":
        grafico_distribuzione_tipi(gestionale)    # genera grafico a torta
    elif scelta == "0":
        return
    else:
        print("Scelta non valida.")


# funzione principale: coordina il flusso dell'applicazione
def menu():
    # deserializzazione iniziale: ripristina lo stato del menu dal file CSV
    carica_csv(gestionale)

    while True: # ciclo infinito per mantenere il programma attivo fino all'uscita
        print("\n== RISTORANTE ==")
        print("1. Visualizza menu")
        print("2. Aggiungi piatto")
        print("3. Modifica piatto")
        print("4. Elimina piatto")
        print("5. Segna disponibile/esaurito")
        print("6. Salva menu su CSV")
        print("7. Ordini")
        print("8. Recensioni")
        print("9. Analisi")
        print("10. Grafici")
        print("0. Esci")
        scelta = input("\nScelta: ").strip()

        # match-case per una gestione pulita delle opzioni (Python 3.10+)
        match scelta:
            case "1":
                gestionale.visualizza_tutti()       # usa __str__ — metodo speciale
            case "2":
                gestionale.crea_piatto()            # avvia la creazione guidata
            case "3":
                codice = input("Codice piatto da modificare: ").strip()
                gestionale.modifica(codice)         # cerca e modifica per codice univoco
            case "4":
                codice = input("Codice piatto da eliminare: ").strip()
                gestionale.elimina(codice)          # rimuove l'oggetto dalla lista
            case "5":
                codice = input("Codice piatto: ").strip()
                gestionale.toggle_disponibile(codice)  # inverte il booleano disponibile
            case "6":
                salva_csv(gestionale)               # serializzazione forzata su richiesta
            case "7":
                menu_ordini()                       # navigazione sottomenu
            case "8":
                menu_recensioni()
            case "9":
                menu_analisi()
            case "10":
                menu_visualizzazione()
            case "0":
                # persistenza dei dati garantita: salva tutto prima della chiusura
                salva_csv(gestionale)
                print("Arrivederci!")
                break # interrompe il ciclo while
            case _:
                print("Scelta non valida.")


# avvio del programma: impedisce l'esecuzione automatica in caso di importazione
if __name__ == "__main__":
    menu()