# Modulo che gestisce inserimento vendite

def inserisci_vendite(data): # chiede i dati all'utente e gestisce errori
    while True: # ciclo cje si ripete finchè dati sono validi
        try: # per gestire eventuali errori
            dd = input(f"Inserisci le vendite del {data} separate da spazio: ")
            vendite = []
            for v in dd.split(): # divide la stringa per spazi
                vendite.append(float(v)) # converte ogni valore in float e lo aggiunge 
                if len(vendite) == 0: # check se vuota
                    print("Nessun dato inserito, riprova!")
                    continue # riparte da inizio while
            return vendite # se tutto okay restituisce la lista
        except ValueError: # in caso di valore NON numerico
            print("Errore! Hai inserito un valore non valido. Cancello e riprova da capo!")
            # riparte col while