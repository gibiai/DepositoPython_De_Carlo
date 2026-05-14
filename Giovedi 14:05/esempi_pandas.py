import pandas as pd
import numpy as np

# Creazione di un dataframe (colonne e serie di dati, quindi passiamo un dizionario)
print("\nIntroduzione ai Dataframe")
data = {
    "Nome": ["Mario", "Bob", "Carla", "Giulio"],
    "Età": [25, 30, 22, 16],
    "Città": ["Roma", "Milano", "Napoli", "Torino"]
}

df = pd.DataFrame(data)

print("Dataframe originale")
print(df)

df_older = df[df['Età'] > 23] # al posto dell'indexing boolean ci rida' direttamente un dataframe con le caratteristiche richieste
print("\nPersone con età maggiore di 23")
print(df_older)

# se richiamo una colonna che non esiste, verrà create df["Maggiorenne"] e posso aggiungerne quante ne voglio (se non esistono)
# restituirà un booleano
df["Maggiorenne"] = df["Età"] >= 18
print("\nNuova Colonna Maggiorenne: ")
print(df) # sto usando sempre quello vecchio

# Pulizia dei dati
print("\nPulizia dei dati con Pandas")
data2 = {
    "Nome": ["Anna", "Bob", "Carla", "Bob", "Carla", "Anna", None],
    "Età": [25, 30, 22, 30, np.nan, 25, 29],
    "Città": ["Roma", "Milano", "Napoli", "Milano", "Napoli", "Roma", "Roma"]
}
df2 = pd.DataFrame(data2)
# stampo dataframe origianle
print("\nDataframe Originale: ")
print(df2)

# rimozione duplicati
df2 = df2.drop_duplicates()

# gestione dei dati mancanti
# rimozione delle righe dove almeno un elemento è mancante
df_cleaned = df2.dropna()

# posso sostituire dati mancanti con valori di default 
# df2["Età"].fillna(df2["Età"].mean(), inplace=True) vecchio metodo 
df2.fillna({"Età": df2["Età"].mean()}, inplace=True)
# variabile inplace serve a dire: sostituisci direttamente dentro il dataframe senza dover riassegnare il risultato

# stampo dataframe pulito
print("\nDataframe post pulizia:")
print(df_cleaned)

# stampo del dataframe con dati mancanti sostituiti

print("\nDataframe con dati mancanti sostituiti:")
print(df2)
