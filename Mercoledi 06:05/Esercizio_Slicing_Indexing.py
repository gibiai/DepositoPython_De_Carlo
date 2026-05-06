# Esercizio
import numpy as np
import csv 

# punto 1 - crea array 1D di 20 numeri interi random tra 10-50
array = np.random.randint(10, 50, size=20) # randint(start, stop, size) - stop escluso quini 51

# punto 2 - primi 10 
primi_10 = array[:10] # slicing - dall'inizio fino indice 10 escluso
print(f"Primi 10 elementi: {primi_10}")

# punto 3 - ultimi 5 elementi con slicing
ultimi_5 = array[-5:] # slicing - ultimi 5 elementi con indice neg
print(f"Ultimi 5 elementi: {ultimi_5}")

# punto 4 - elementi da indice 5 a 15, escluso
da_5_a_15 = array[5:15] # slicing - da 5 a 15, questo escluso
print(f"Elementi da indice 5 a 15: {da_5_a_15}")

# punto 5 - ogni terzo elemento
ogni_3 = array[::3] # slicing - step 3 significa prende ogni 3
print(f"Ogni terzo elemento: {ogni_3}")

# punto 6 - modifica elementi dall'indice 5 all'indice 10 esclusoi, con valore 99
array[5:10] = 99 # slicing - assegna 99 a tutti gli elementi in quella posizione
print(f"Array dopo modifica: {array}")

# extra - salva su file txt
with open("slicing.txt", "w") as file: # "w" crea o sovrascrive il file
    file.write("SLICING NUMPY\n") # intestazione
    file.write(f"Array originale: {array}\n") # scriviamo stringa per stringa gli array con f-string (__str__)
    file.write(f"Primi 10 elementi: {primi_10}\n")
    file.write(f"Ultimi 5 elementi: {ultimi_5}\n")
    file.write(f"Elementi da indice 5 a 15: {da_5_a_15}\n")
    file.write(f"Ogni terzo elemento: {ogni_3}\n")
    file.write(f"Array dopo modifica: {array}\n")
print("Dati salvati su slicing.txt!")

# extra - salva su csv con tolist (metodi specifico di NumPy)
with open("slicing.csv", "w", newline="") as file: # "w" crea o sovrascrive il file, newline evita righe vuote
    writer = csv.writer(file) # crea writer csv
    writer.writerow(["sottoarray", "valori"]) # scrive intestazione
    writer.writerow(["array_originale", array.tolist()]) # tolist() converte array numpy in lista per csv
    writer.writerow(["primi_10", primi_10.tolist()])
    writer.writerow(["ultimi_5", ultimi_5.tolist()])
    writer.writerow(["da_5_a_15", da_5_a_15.tolist()])
    writer.writerow(["ogni_3", ogni_3.tolist()])
print("Dati salvati su slicing.csv!")