# modulo per la visualizzazione grafica dei dati del menu
# genera due grafici: prezzo medio per tipo e distribuzione piatti per tipo
import matplotlib.pyplot as plt


# grafico a barre: mostra il prezzo medio per ogni tipo di piatto
def grafico_prezzi_per_tipo(gestionale):

    # controlla che ci siano piatti da mostrare per evitare errori nei calcoli
    if not gestionale.piatti:
        print("Nessun piatto nel menu.")
        return

    # dizionario che accumula i prezzi per tipo per calcolare la media
    prezzi_per_tipo = {}
    # dizionario che conta quanti piatti ci sono per ogni tipo
    conteggio_per_tipo = {}

    # scorre tutti i piatti e raggruppa i prezzi per tipo
    for piatto in gestionale.piatti:
        # get_tipo() è polimorfico: ogni sottoclasse risponde con la sua stringa specifica
        tipo = piatto.get_tipo()

        # se il tipo esiste già aggiunge il prezzo alla somma e incrementa il contatore
        if tipo in prezzi_per_tipo:
            prezzi_per_tipo[tipo]    += piatto.prezzo
            conteggio_per_tipo[tipo] += 1
        # altrimenti crea la nuova chiave nel dizionario e inizializza i valori
        else:
            prezzi_per_tipo[tipo]    = piatto.prezzo
            conteggio_per_tipo[tipo] = 1

    # Estrae i nomi dei tipi (le chiavi del dizionario) e calcola la media per ognuno
    tipi  = list(prezzi_per_tipo.keys())
    medie = []
    for tipo in tipi:
        # Calcola la media aritmetica dividendo il totale dei prezzi per il numero di piatti di quel tipo
        media = prezzi_per_tipo[tipo] / conteggio_per_tipo[tipo]
        medie.append(round(media, 2)) # Arrotonda a due decimali per una corretta visualizzazione monetaria

    # Configura l'area del grafico con dimensioni fisse (7x5 pollici)
    plt.figure(figsize=(6, 6))
    # Disegna le barre: associa ogni tipo all'altezza della sua media calcolata
    # Specifica una palette di colori per distinguere visivamente le portate
    plt.bar(tipi, medie, color=["steelblue", "coral", "mediumseagreen"])

    # Cicla sulle posizioni e i valori per stampare il prezzo medio formattato sopra ogni colonna del grafico
    for i, valore in enumerate(medie):
        # i = posizione x, valore + 0.2 = posizione y (leggermente sopra la barra)
        plt.text(i, valore + 0.2, f"€{valore:.2f}", ha="center", fontsize=10)

    # Impostazione di etichette, titoli e ottimizzazione spazi
    plt.title("Prezzo medio per tipo di piatto")
    plt.xlabel("Tipo")
    plt.ylabel("Prezzo medio (€)")
    plt.tight_layout() # sistema i margini per evitare che le scritte vengano tagliate
    plt.show() # blocca l'esecuzione finché l'utente non chiude la finestra del grafico
    print("Grafico prezzi per tipo generato!")


# grafico a torta: mostra la distribuzione percentuale dei piatti per tipo
def grafico_distribuzione_tipi(gestionale):

    # controllo di sicurezza per evitare di generare grafici vuoti
    if not gestionale.piatti:
        print("Nessun piatto nel menu.")
        return

    # dizionario che conta quanti piatti ci sono per ogni tipo (frequenza)
    conteggio = {}

    for piatto in gestionale.piatti:
        tipo = piatto.get_tipo()
        # Logica di incremento contatore: se non c'è, lo crea, se c'è, aggiunge 1
        if tipo in conteggio:
            conteggio[tipo] += 1
        else:
            conteggio[tipo] = 1

    # separa le chiavi (nomi) dai valori (numeri) per passarli ai parametri di plt.pie
    tipi   = list(conteggio.keys())
    valori = list(conteggio.values())

    # crea il grafico a torta con area quadrata (6x6) per un cerchio perfetto
    plt.figure(figsize=(6, 6))
    # autopct calcola e formatta la percentuale (1.1f significa 1 cifra decimale)
    plt.pie(valori, labels=tipi, autopct="%1.1f%%", 
            colors=["steelblue", "coral", "mediumseagreen"],
            startangle=90) # ruota la torta per farla iniziare dall'alto

    plt.title("Distribuzione piatti per tipo")
    plt.tight_layout() # previene sovrapposizioni tra etichette e titoli
    plt.show() # visualizza il grafico a schermo
    print("Grafico distribuzione tipi generato!")
