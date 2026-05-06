import numpy as np # libreria numpy per array e operazioni matematiche
import csv # libreria per gestione file csv

# punto 1 - crea array di numeri interi da 10 a 49
array = np.arange(10, 50) # arange(start, stop) - stop escluso quindi 50 per arrivare a 49
print(f"Array: {array}")

# punto 2 - verifica tipo di dato
print(f"Tipo di dato: {array.dtype}") # dtype restituisce il tipo - int64 di default

# punto 3 - sovrascrive array convertendolo in float64 tramite casting
# alternativa era .astype(), usiamo il costruttore np.float64() passandogli l'array originale
array_float = np.float64(array) # riga 1: creo il nuovo array float
array = array_float             # riga 2: assegno il nuovo array alla variabile principale 
print(f"Nuovo tipo di dato: {array.dtype}") # ora sarà float64

# punto 4 - stampa la forma dell'array
print(f"Forma dell'array: {array.shape}") # shape restituisce le dimensioni - (40,) significa 40 elementi

# extra - salva array su file txt
with open("array.txt", "w") as file: # "w" crea o sovrascrive il file
    file.write("ARRAY NUMPY\n") # intestazione
    file.write(f"Tipo di dato: {array.dtype}\n") # scrive tipo
    file.write(f"Forma: {array.shape}\n") # scrive forma
    file.write(f"Valori: {array}\n") # scrive tutti i valori
print("Array salvato su array.txt!")

# extra - salva array su csv con contatore
with open("array.csv", "w", newline="") as file: # "w" crea o sovrascrive il file
    writer = csv.writer(file) # crea writer csv
    writer.writerow(["indice", "valore"]) # scrive intestazione
    i = 0 # contatore manuale parte da 0
    for valore in array: # scorre ogni valore dell'array
        writer.writerow([i, valore]) # scrive riga con indice e valore
        i += 1 # incrementa contatore ad ogni iterazione
print("Array salvato su array.csv!")