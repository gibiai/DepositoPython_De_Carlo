# amministrazione.py - Modulo gestione amministrazione e rapporti

def rapporto_vendite(): # genera rapporto vendite leggendo file clienti txt riga per riga
    print("\n--- RAPPORTO VENDITE ---")
    guadagno_totale = 0 # accumulatore guadagno totale inizializzato a zero

    try:
        with open("clienti.txt", "r") as file: # "r" legge il file clienti
            righe = file.readlines() # legge tutte le righe

        if len(righe) == 0: # controlla che ci siano clienti
            print("Nessun acquisto registrato.")
            return

        for riga in righe: # scorre ogni riga cliente
            dati = riga.strip().split(",") # divide per virgola
            nome = dati[0] # primo elemento è il nome
            cognome = dati[1] # secondo elemento è il cognome
            acquisti = dati[2:] # resto della riga sono gli acquisti

            totale_cliente = 0 # totale acquisti del singolo cliente
            print(f"\nCliente: {nome} {cognome}")

            for acquisto in acquisti: # scorre acquisti del cliente
                if ":" in acquisto: # controlla che l'acquisto sia valido
                    parti = acquisto.split(":") # divide articolo e prezzo
                    articolo = parti[0] # nome articolo
                    prezzo = float(parti[1]) # prezzo articolo
                    totale_cliente += prezzo # aggiunge al totale cliente
                    print(f"  - {articolo}: {prezzo:.2f}€")

            guadagno_totale += totale_cliente # aggiunge al totale generale
            print(f"  Totale: {totale_cliente:.2f}€")

        print(f"\nGuadagno totale: {guadagno_totale:.2f}€") # stampa totale generale

        with open("rapporto.txt", "a") as file: # salva rapporto su file txt
            file.write(f"Guadagno totale: {guadagno_totale:.2f}€\n") # aggiunge al file

    except FileNotFoundError: # se il file non esiste
        print("Nessun acquisto registrato.")