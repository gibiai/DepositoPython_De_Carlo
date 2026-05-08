# modulo che gestisce la lettura e scrittura dei file
# menu.csv — catalogo piatti
# ordini.txt — storico ordini del giorno
# recensioni.txt — recensioni clienti
import csv
import os
from models import Antipasto, Primo, Secondo

# controllo sul percorso della cartella dove si trova questo file
# funziona sempre indipendentemente da dove viene lanciato il programma
CARTELLA = os.path.dirname(os.path.abspath(__file__))

# percorsi completi dei tre file
PATH_CSV        = os.path.join(CARTELLA, "menu.csv")
PATH_ORDINI     = os.path.join(CARTELLA, "ordini.txt")
PATH_RECENSIONI = os.path.join(CARTELLA, "recensioni.txt")


# Deserializzazione
# legge menu.csv e ricostruisce gli oggetti Piatto nella lista del gestionale
def carica_csv(gestionale):
    # controlla che il file esista prima di aprirlo
    if not os.path.exists(PATH_CSV):
        print("(i) Nessun menu.csv trovato — si parte da zero.")
        return # se non esiste esce dalla funzione senza fare nulla

    with open(PATH_CSV, mode="r", encoding="utf-8") as f:
        # DictReader legge ogni riga come dizionario usando la prima riga come chiavi
        reader = csv.DictReader(f)
        for riga in reader:
            # ricostruisce l'oggetto giusto in base al tipo salvato nel CSV
            tipo = riga["tipo"]
            if tipo == "Antipasto":
                piatto = Antipasto(riga["codice"], riga["nome"], riga["categoria"], float(riga["prezzo"]), riga["extra"])
            elif tipo == "Primo":
                piatto = Primo(riga["codice"], riga["nome"], riga["categoria"], float(riga["prezzo"]), riga["extra"])
            elif tipo == "Secondo":
                piatto = Secondo(riga["codice"], riga["nome"], riga["categoria"], float(riga["prezzo"]), riga["extra"])
            else:
                # se il tipo non è riconosciuto salta la riga senza crashare
                continue
            # aggiunge direttamente alla lista del gestionale senza stampare messaggi
            gestionale.piatti.append(piatto)

    print(f"(i) Menu caricato: {len(gestionale.piatti)} piatti trovati.")

# Serializzazione dati
# scrive tutti i piatti del gestionale su menu.csv
def salva_csv(gestionale):
    # controlla che ci sia qualcosa da salvare
    # interrompe la funzione se la lista è vuota, evitando di sovrascrivere o creare un file CSV senza dati.
    if not gestionale.piatti:
        print("Nessun piatto da salvare!")
        return

    # colonne del CSV — extra contiene l'attributo specifico di ogni sottoclasse
    colonne = ["codice", "nome", "categoria", "prezzo", "tipo", "extra"]

    with open(PATH_CSV, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=colonne) # creo "assistente" che trasforma i dizionari in righe del CSV
        writer.writeheader() # Scrive prima riga CSV utilizzando nomi definiti nella lista colonne

        for piatto in gestionale.piatti:
            # determina il valore di "extra" in base al tipo reale del piatto
            # hasattr() controlla se l'oggetto ha quell'attributo senza crashare
            if hasattr(piatto, "porzione"):
                extra = piatto.porzione
            elif hasattr(piatto, "tipo_pasta"):
                extra = piatto.tipo_pasta
            elif hasattr(piatto, "cottura"):
                extra = piatto.cottura
            else:
                extra = ""

            writer.writerow({
                "codice":    piatto.codice,
                "nome":      piatto.nome,
                "categoria": piatto.categoria,
                "prezzo":    piatto.prezzo,
                # get_tipo() è polimorfico: ogni classe risponde col suo tipo
                "tipo":      piatto.get_tipo(),
                "extra":     extra
            })

    print(f"Menu salvato! ({len(gestionale.piatti)} piatti)")


# TXT
# legge ordini.txt e stampa a schermo tutto lo storico
def leggi_ordini():
    if not os.path.exists(PATH_ORDINI): # validazione sull'effettiva presenza file
        print("(i) Nessun file ordini trovato.")
        return

    print("\n--- STORICO ORDINI ---")
    with open(PATH_ORDINI, mode="r", encoding="utf-8") as f:
        contenuto = f.read()
        # controlla che il file non sia vuoto
        if not contenuto.strip():
            print("Nessun ordine registrato.")
        else:
            print(contenuto)


# aggiunge un nuovo ordine in fondo al file ordini.txt
def aggiungi_ordine():
    tavolo = input("Numero tavolo: ").strip()
    piatto = input("Piatto ordinato: ").strip()
    # "a" = append: aggiunge in fondo senza cancellare il contenuto esistente
    with open(PATH_ORDINI, mode="a", encoding="utf-8") as f:
        f.write(f"Tavolo {tavolo} → {piatto}\n")
    print("Ordine registrato ✅")


# svuota completamente il file ordini.txt dopo conferma utente
def reset_ordini():
    conferma = input("Sei sicuro di voler azzerare gli ordini? (s/n): ").strip().lower()
    if conferma == "s":
        # "w" sovrascrive il file con contenuto vuoto
        with open(PATH_ORDINI, mode="w", encoding="utf-8") as f:
            f.write("")
        print("Ordini azzerati ✅")
    else:
        print("Operazione annullata.")


# ─── TXT RECENSIONI ──────────────────────────────────────────────────────────

# legge recensioni.txt e stampa a schermo tutte le recensioni
def leggi_recensioni():
    if not os.path.exists(PATH_RECENSIONI):
        print("(i) Nessuna recensione trovata.")
        return

    print("\n--- RECENSIONI CLIENTI ---")
    with open(PATH_RECENSIONI, mode="r", encoding="utf-8") as f: # apriamo "f" in modalità lettura
        contenuto = f.read()
        if not contenuto.strip(): # controlla se file è vuoto - se non ha contenuto
            print("Nessuna recensione registrata.")
        else:
            print(contenuto)


# aggiunge una nuova recensione in fondo al file recensioni.txt
def aggiungi_recensione():
    cliente = input("Nome cliente: ").strip()
    voto    = input("Voto (1-5): ").strip()
    testo   = input("Recensione: ").strip()
    with open(PATH_RECENSIONI, mode="a", encoding="utf-8") as f:
        f.write(f"[{cliente}] Voto: {voto}/5 — {testo}\n")
    print("Recensione aggiunta!")