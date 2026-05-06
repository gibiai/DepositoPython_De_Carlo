import numpy as np 

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing base
print(arr[2:7]) # 2 3 4 5 6

# Slicing con passo
print(arr[1:8:2]) # 1 3 5 7

# Slicing start e stop
print(arr[:5]) # 0 1 2 3 4
print(arr[5:]) # 5 6 7 8 9

# Indici negativi
print(arr[-5]) # 5 6 7 8 9
print(arr[:-5]) # 0 1 2 3 4

# Slicing riprende sempre valori rettangolari o quadrata
# array[start:stop:step]
# non può essere arbitrario, sempre collegato logica