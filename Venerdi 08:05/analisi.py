# modulo che si occupa di analizzare i dati del gestionale
# usa filter() per filtrare i piatti e calcola statistiche sul menu
# "setacciando" solo i piatti che servono per la riuscita delle analisi
from file_manager import leggi_ordini, leggi_recensioni

# analizza tutti i piatti presenti nel gestionale e mostra il totale
def analizza_tutti(gestionale):
    if not gestionale.piatti: # controlla che ci siano piatti da analizzare
        print("Nessun piatto nel menu!")
        return

    print("\n--- ANALISI COMPLETA MENU ---")
    totale_piatti = len(gestionale.piatti) # riporta numero totale dei piatti

    # calcola il prezzo medio sommando tutti i prezzi e dividendo per il totale
    # generator expression - ciclo for contratto nelle parentesi
    # estrae .prezzo da ogni oggetto piatto e lo passa alla funzione sum
    somma_prezzi  = sum(p.prezzo for p in gestionale.piatti) # calcoliamo i valori in posizione
    prezzo_medio  = somma_prezzi / totale_piatti # divisione semplice per avere la media

    # cerca il piatto più caro e quello più economico scorrendo la lista
    piu_caro      = gestionale.piatti[0] # punto di partenza - primo elemento lista
    piu_economico = gestionale.piatti[0] # lo usiamo come base di confronto
    for piatto in gestionale.piatti: # scorriamo tutta la lista
        if piatto.prezzo > piu_caro.prezzo:
            piu_caro = piatto # aggiorniamo se troviamo più caro
        if piatto.prezzo < piu_economico.prezzo:
            piu_economico = piatto # aggiorniamo se troviamo più economico

    # serie di f-string per stampare tutto anche dove necessita di numero decimale con 2 dopo
    print(f"Totale piatti in menu:  {totale_piatti}")
    print(f"Prezzo medio:           €{prezzo_medio:.2f}")
    print(f"Piatto più caro:        {piu_caro.nome} (€{piu_caro.prezzo:.2f})")
    print(f"Piatto più economico:   {piu_economico.nome} (€{piu_economico.prezzo:.2f})")


# filtra i piatti per tipo usando filter() e mostra solo quelli richiesti
def analizza_per_tipo(gestionale):
    print("\nTipi disponibili: Antipasto, Primo, Secondo") # mostriamo utente i tipi disponibili
    tipo_richiesto = input("Inserisci tipo: ").strip() # chiediamo quale vuole

    # filter() scorre la lista e tiene solo i piatti il cui get_tipo() corrisponde
    # get_tipo() è polimorfico: ogni classe risponde col suo tipo (Antipasto, Primo, Secondo)
    risultati = list(filter( # il risultato finisce in risultati solo se True
        lambda p: p.get_tipo().lower() == tipo_richiesto.lower(), # in questo caso la funzione criterio è lambda
        gestionale.piatti # lista su cui filtriamo
    ))

    # controlla se filter ha trovato qualcosa
    if not risultati:
        print(f"Nessun piatto di tipo '{tipo_richiesto}' trovato.")
        return

    # visualizzazione dei risultati finali
    print(f"\n--- PIATTI: {tipo_richiesto.upper()} ---") # scriviamo in maiuscolo
    for piatto in risultati: # mostra ogni piatto trovato descrivendolo
        piatto.descrivi()
    print(f"\nTotale: {len(risultati)} piatti") # feedback finale che mostra numero piatti

# filtra i piatti per fascia di prezzo usando filter()
def analizza_per_prezzo(gestionale):
    print("\n--- ANALISI PER FASCIA DI PREZZO ---")
    # chiede i limiti della fascia di prezzo
    minimo  = float(input("Prezzo minimo (€): "))
    massimo = float(input("Prezzo massimo (€): "))

    # filter() tiene solo i piatti il cui prezzo è dentro la fascia richiesta
    risultati = list(filter(
        lambda p: minimo <= p.prezzo <= massimo,
        gestionale.piatti
    ))

    if not risultati:
        print(f"Nessun piatto tra €{minimo:.2f} e €{massimo:.2f}.")
        return

    print(f"\nPiatti tra €{minimo:.2f} e €{massimo:.2f}:")
    for piatto in risultati:
        piatto.descrivi()
    print(f"\nTotale: {len(risultati)} piatti")

# filtra i piatti per disponibilità usando filter() su campo booleano
# usa print(piatto) che chiama __str__ — metodo speciale per la rappresentazione testuale
def analizza_disponibili(gestionale):
    if not gestionale.piatti: # controlla che ci siano piatti prima di filtrare
        print("Nessun piatto nel menu!")
        return

    # filter() con lambda booleana: tiene solo i piatti con disponibile == True
    disponibili = list(filter(lambda p: p.disponibile, gestionale.piatti))
    # not p.disponibile inverte il booleano: tiene solo i piatti esauriti
    esauriti    = list(filter(lambda p: not p.disponibile, gestionale.piatti))

    print(f"\n--- DISPONIBILITÀ MENU ---")
    print(f"Disponibili: {len(disponibili)}")
    print(f"Esauriti:    {len(esauriti)}")

    if esauriti:
        print("\nPiatti esauriti:")
        for p in esauriti:
            print(f"  {p}")  # print(p) chiama __str__ automaticamente — versione compatta

# mostra un riepilogo degli ordini e delle recensioni dai file TXT
def analizza_file(gestionale):
    print("\n--- ANALISI FILE ---")
    print("1. Storico ordini")
    print("2. Recensioni clienti")
    scelta = input("Scelta: ").strip()

    if scelta == "1":
        leggi_ordini()
    elif scelta == "2":
        leggi_recensioni()
    else:
        print("Scelta non valida.")
        
