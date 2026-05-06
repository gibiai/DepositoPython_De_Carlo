# Fancy Indexing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) # [20 40]

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) # [10 30 50]

# può scegliere valori non contigui e in ordine arbitrario
# crea sempre una copia dei dati
# utilizza indici interi