import pandas as pd
import numpy as np

# Dati di esempio
data_vendite = {

    'Data': ['2021-01-01', '2021-01-01', '2021-01-01', '2021-01-02', '2021-01-02'],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Milano'],
    'Prodotto': ['Mouse', 'Tastiera', 'Mouse', 'Tastiera', 'Mouse'],
    'Vendite': [100, 200, 150, 300, 250]

}

df_vendite = pd.DataFrame(data_vendite)

# Pivot Table 
pivot_df = df_vendite.pivot_table(values='Vendite', index='Prodotto', columns='Città', aggfunc='mean')
print("\nPivot media vendite prodotto pre città")
print(pivot_df)

# Group by
print("\nGroup by somma prodotto")
grouped_df = df_vendite.groupby('Prodotto').sum()
print(grouped_df)

# Salvataggio csv
df_vendite.to_csv("df_vendite.csv")

print(pd.read_csv("df_vendite.csv"))
# print(pd.read_csv("df_vendite.csv").head())
print(df_vendite.describe())

# Sorted
df_sorted = df_vendite.sort_values(by="Vendite")
print("\nDataFrame Ordinato per Vendite")
print(df_sorted)

# Merge
merge_df = pd.merge(df_vendite, pd.read_csv("vendite_sample.csv"), on="Città")
print(merge_df)

# Apply
# applicazione di una funzione a una colonna

# Creazione dataframe di esempio per apply
data_eta = {
    "Nome": ["Mario", "Anna", "Luigi", "Sara"],
    "Età": [15, 35, 45, 70]
}
df = pd.DataFrame(data_eta)

def categoria_eta(eta):
    if(eta < 18):
        return "Giovane"
    elif(eta < 40):
        return "Adulto"
    else:
        return "Anziano"

df["Categoria Età"] = df["Età"].apply(categoria_eta)
# df['età_doppia] = df['età'].apply(lambda x: x * 2)

print("\nCategoria eta nuova colonna ")
print(df)

df_vendite["Vendite_IVA"] = df_vendite["Vendite"].apply(lambda x: x + x * 22 / 100)
print("\nVendite + Iva ")
print(df_vendite)

# Esempio complessivo pivot e risistemazione

# Dataframe
data_vendite2 = {

    'Prodotto': ['Tastiera', 'Mouse', 'Monitor', 'Tastiera', 'Monitor'],
    'Quantità': [5, 10, 2, 7, 3],
    'Città': ['Roma', 'Milano', 'Roma', 'Napoli', 'Milano'],
    'Data': ['2021-09-01', '2021-09-01', '2021-09-02', '2021-09-02', '2021-09-03']

}
df_vendite2 = pd.DataFrame(data_vendite2)

data_costi = {

    'Prodotto': ['Tastiera', 'Mouse', 'Monitor'],
    'Costo per unità': [50, 25, 150]
}

costi_df =  pd.DataFrame(data_costi)

df_merge_vendite = pd.merge(df_vendite2, costi_df, on='Prodotto')
print("\n Merge vendite e costi")
print(df_merge_vendite)

pivot_vendite =  df_merge_vendite.pivot_table(index="Prodotto", columns='Città', values="Quantità", aggfunc='sum')
print("\nPivot table")
print(pivot_vendite)

pivot_vendite.to_csv("pivot_vendite.csv")