# Modulo per analisi dei dati

def calcola_totale(giorni): # calcola il totale di tutti i giorni
    totale = 0
    for giorno in giorni: # scorre tutti i giorni
        totale += giorno.totale() # aggiunge il totale di ogni giorno
    return totale

def calcola_media(giorni): # calcola la media di tutti i giorni
    if len(giorni) == 0: # controlla che non sia vuota
        return 0
    return calcola_totale(giorni) / len(giorni) # totale con diviso numero giorni

def giorni_sopra_media(giorni): # trova i giorni con vendite sopra la media generale
    media = calcola_media(giorni) # media generale
    risultato = [] # lista vuota per i giorni sopra la media
    for giorno in giorni: # scorre tutti i giorni
        if giorno.totale() > media: # se il totale supera la media
            risultato.append(giorno) # aggiunge alla lista
    return risultato
