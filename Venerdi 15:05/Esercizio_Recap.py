import pandas as pd
import numpy as np
import random

# DATI DA CREARE
# liste di valori realistici da cui peschiamo casualmente
nomi         = ["Mario", "Lucia", "Marco", "Anna", "Giulio", "Sara", "Luca", "Elena", "Paolo", "Chiara"]
abbonamenti  = ["Base", "Premium", "Family"]
citta        = ["Roma", "Milano", "Napoli", "Torino", "Firenze"]

# costruiamo le liste una per una con cicli for classici
nomi_lista        = []
eta_lista         = []
citta_lista       = []
abbonamento_lista = []

for _ in range(10):
    nomi_lista.append(random.choice(nomi))           # nome casuale dalla lista
    eta_lista.append(random.randint(16, 70))         # età casuale tra 16 e 70
    citta_lista.append(random.choice(citta))         # città casuale dalla lista
    abbonamento_lista.append(random.choice(abbonamenti))  # abbonamento casuale

# aggiungiamo manualmente 1 duplicato alla fine come richiesto dalla traccia
nomi_lista.append(nomi_lista[0])
eta_lista.append(eta_lista[0])
citta_lista.append(citta_lista[0])
abbonamento_lista.append(abbonamento_lista[0])

# aggiungiamo manualmente 1 valore mancante sull'età nella seconda posizione
eta_lista[1] = None

# creiamo il DataFrame iscritti passando le liste al dizionario
iscritti = pd.DataFrame({
    "Nome":             nomi_lista,
    "Eta":              eta_lista,
    "Citta":            citta_lista,
    "Tipo_Abbonamento": abbonamento_lista
})

# DataFrame presenze — almeno 15 righe, 3 date, 3 città
corsi       = ["Yoga", "CrossFit", "Nuoto", "Pilates"]
citta_corsi = ["Roma", "Milano", "Napoli"]
date        = ["2024-01-10", "2024-01-15", "2024-02-05", "2024-02-20", "2024-03-01"]

corsi_lista        = []
citta_corsi_lista  = []
date_lista         = []
partecipanti_lista = []

for _ in range(15):
    corsi_lista.append(random.choice(corsi))
    citta_corsi_lista.append(random.choice(citta_corsi))
    date_lista.append(random.choice(date))
    partecipanti_lista.append(random.randint(5, 30))

presenze = pd.DataFrame({
    "Data":         date_lista,
    "Corso":        corsi_lista,
    "Citta":        citta_corsi_lista,
    "Partecipanti": partecipanti_lista
})

# DataFrame costi_abbonamento — tabella fissa con i tre tipi di abbonamento
costi_abbonamento = pd.DataFrame({
    "Tipo_Abbonamento": ["Base", "Premium", "Family"],
    "Costo_Mensile":    [30, 60, 90]
})

print("=" * 50)
print("CENTRO SPORTIVO — Analisi Dati")
print("=" * 50)

# 1. INTRODUZIONE
# a. stampa iscritti originali prima di qualsiasi modifica
print("\n--- Iscritti originali ---")
print(iscritti)

# b. filtra gli iscritti con età maggiore di 25
# boolean indexing —  filtra, restituisce solo le righe che soddisfano la condizione
iscritti_over25 = iscritti[iscritti["Eta"] > 25]
print("\n--- Iscritti con età maggiore di 25 ---")
print(iscritti_over25)

# c. colonna Attivo: True se età <= 60, False se oltre
# regola scelta: iscritto attivo se ha meno di 60 anni
# pandas valuta la condizione riga per riga e crea la colonna booleana
# stampando true e false 
iscritti["Attivo"] = iscritti["Eta"] <= 60
print("\n--- Iscritti con colonna Attivo ---")
print(iscritti[["Nome", "Eta", "Attivo"]])

# 2. PULIZIA DATI
# a. rimozione duplicati — drop_duplicates() rimuove le righe identiche
print(f"\n--- Righe prima della rimozione duplicati: {len(iscritti)} ---")
iscritti = iscritti.drop_duplicates()
print(f"--- Righe dopo la rimozione duplicati:  {len(iscritti)} ---")

# b. verifica valori mancanti — isnull() trova i NaN, sum() li conta per colonna
# dovrebbe apparire quello in età (1) inserito manualmente
print("\n--- Valori mancanti prima del fillna ---")
print(iscritti.isnull().sum())

# c. se Eta è mancante sostituisce con la media della colonna Eta
# mean() calcola la media di tutti i valori presenti nella colonna
# inplace=True modifica direttamente il DataFrame senza riassegnarlo
iscritti.fillna({"Eta": iscritti["Eta"].mean()}, inplace=True)

print("\n--- Valori mancanti dopo il fillna ---")
print(iscritti.isnull().sum())

# 3. APPLY CON FUNZIONE PERSONALIZZATA
# funzione che classifica l'età in tre fasce come richiesto dalla traccia
def fascia_eta(eta):
    if eta < 18:
        return "Junior"    # minore di 18
    elif eta <= 44:
        return "Adulto"    # da 18 a 44
    else:
        return "Senior"    # 45 o più

# apply() applica la funzione fascia_eta a ogni singolo valore della colonna Eta
# il risultato viene salvato nella nuova colonna Fascia_Eta
iscritti["Fascia_Eta"] = iscritti["Eta"].apply(fascia_eta)

print("\n--- Iscritti con colonna Fascia_Eta ---")
print(iscritti[["Nome", "Eta", "Fascia_Eta"]])

# 4. ANALISI PRESENZE
# a. ordina presenze per Citta e poi per Partecipanti
# sort_values con lista ordina prima per Citta poi per Partecipanti a parità di città
# ordino orima citta alfabetico e poi partecipanti numerico crescente
presenze_ordinate = presenze.sort_values(by=["Citta", "Partecipanti"])
print("\n--- Presenze ordinate per Citta e Partecipanti ---")
print(presenze_ordinate)

# b. groupby per Corso con somma totale partecipanti
# raggruppa le righe con lo stesso corso e somma i partecipanti di ogni gruppo
print("\n--- Totale partecipanti per Corso ---")
totale_per_corso = presenze.groupby("Corso")["Partecipanti"].sum()
print(totale_per_corso)

# c. groupby per Citta con media partecipanti
# raggruppa per città e calcola la media dei partecipanti per ogni gruppo
print("\n--- Media partecipanti per Città ---")
media_per_citta = presenze.groupby("Citta")["Partecipanti"].mean().round(2)
print(media_per_citta)

# d. Creo pivot table: mostra la media partecipanti per ogni combinazione Corso-Città
# indice = righe, columns = colonne, values = valori, aggfunc = tipo di aggregazione
# calcola media dove più valori per la stessa combinazione corso-città. Dove non ci sono dati appare NaN.
pivot = presenze.pivot_table(
    index="Corso",       # i corsi diventano le righe
    columns="Citta",     # le città diventano le colonne
    values="Partecipanti",  # i valori dentro la tabella sono i partecipanti
    aggfunc="mean"       # aggregazione: calcoliamo la media
).round(2)

print("\n--- Pivot Table: media partecipanti per Corso e Città ---")
print(pivot)

# 5. MULTIINDEX
# creiamo un nuovo DataFrame con Sede, Anno e numero Iscritti
# ogni Sede appare per entrambi gli anni 
data_multi = {
    "Sede":     ["Nord", "Nord", "Centro", "Centro", "Sud", "Sud"],
    "Anno":     [2024, 2025, 2024, 2025, 2024, 2025],
    "Iscritti": [120, 135, 98, 110, 75, 88]
}

df_multi = pd.DataFrame(data_multi)

# set_index con una lista crea un indice a due livelli (MultiIndex)
# le colonne Sede e Anno diventano l'indice invece di valori normali
df_multi = df_multi.set_index(["Sede", "Anno"])

print("\n--- DataFrame con MultiIndex ---")
print(df_multi)

# i. tutte le righe di una sede — loc con un solo livello restituisce tutte le righe di quella sede
print("\n--- Tutte le righe della sede Nord ---")
print(df_multi.loc["Nord"])

# ii. valore Iscritti di una sede in un anno specifico
# loc con tupla (sede, anno) accede alla cella esatta del MultiIndex
# risultato sarà singolo numero corrispondente
print("\n--- Iscritti sede Centro anno 2025 ---")
print(df_multi.loc[("Centro", 2025), "Iscritti"])

# PUNTO 6: MERGE
# pd.merge crea un nuovo DataFrame collegando iscritti e costi_abbonamento
# (come INNER JOIN, mantiene solo corrispondenza da entrambe le tabelle)
# on="Tipo_Abbonamento" è la colonna ponte tra le due tabelle
# per ogni iscritto trova e aggiunge il Costo_Mensile corrispondente
iscritti_con_costi = pd.merge(iscritti, costi_abbonamento, on="Tipo_Abbonamento")

# crea colonna Costo_Annuale moltiplicando il costo mensile per 12 — operazione vettoriale
iscritti_con_costi["Costo_Annuale"] = iscritti_con_costi["Costo_Mensile"] * 12

print("\n--- Iscritti con costi abbonamento ---")
print(iscritti_con_costi[["Nome", "Tipo_Abbonamento", "Costo_Mensile", "Costo_Annuale"]])

# 7. OUTPUT FINALE
# salviamo i tre file CSV come richiesto dalla traccia
# index=False evita di salvare la colonna con i numeri di riga
iscritti.to_csv("iscritti_puliti.csv", index=False, encoding="utf-8")
print("\niscritti_puliti.csv salvato")
# Oppure in una sottocartella specifica
# iscritti.to_csv("/Users/NomeUtente/cartella_progetto/csv/iscritti_puliti.csv", index=False, encoding="utf-8")

pivot.to_csv("report_presenze_pivot.csv", encoding="utf-8")
print("report_presenze_pivot.csv salvato")

iscritti_con_costi.to_csv("iscritti_con_costi.csv", index=False, encoding="utf-8")
print("iscritti_con_costi.csv salvato")