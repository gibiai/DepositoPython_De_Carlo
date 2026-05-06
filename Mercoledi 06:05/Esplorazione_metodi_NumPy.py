# importo libreria
import numpy as np

# Creazione di un array 
arr = np.array([1, 2, 3, 4, 5]) # 

# Esempi metodi
print("Forma dell'array:", arr.shape) # Output: (5,)
print("Dimensioni array:", arr.ndim) # Output: 1
print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda piattaforma)
print("Numeri di elementi:", arr.size) # Output: 5
print("Somma degli elementi:", arr.sum()) # Output: 15
print("Media degli elementi:", arr.mean()) # Output 3.0
print("Valore massimo:", arr.max())
print("Indice del valore massimo:", arr.argmax()) # Output: 4

"""

DTYPE printa tipo di dato presente array. Può essere float, int, bool, etc.

arr = np.arr([1, 2, 3], dtype='int32')
print(arr.type) # Output: int32

SHAPE serve a sapere forma di un array e dimensioni
arr = np.array([[1, 2, 3] [4, 5, 6]])
print(arr.shape) # Output: (2, 3)

ARANGE crea un array contente sequenza di numeri, accetta 'start, stop, step'

arr = np.arange(10)
print(arr) # Outpu: [0 1 2 3 4 5 6 7 8 9]

RESHAPE cambia la forma di un array senza modificare i dati

arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr) # Output: [[0 1 2] [3 4 5]]

"""