# Al posto di ciclo e if adesso utilizziamo booleano per printare tutti elementi array
# superiore alla posizione 2 (nell'esempio) - start indexing sempre valorizzato
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0]) # Output 1

# Slicing
print(arr[0]) # 1

# Boolean indexing
print(arr[arr > 2])

# !!! indexing anche sopra i multidimensionali !!!
# slicing righe, colonne o misto
# es. riportiamo solo riga 2 e riga 3

arr_2d = np.arra([1, 2, 3, 4]
                 [5, 6, 7, 8]
                 [9, 10, 11, 12])

# Slicing sulle righe
print(arr_2d[1:3]) # Output [[ 5 6 7 8]
                    #       [9 10 11 12]]
                    
# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output [[ 2 3]
                      #        [6 7]
                      #        [10 11]]

# Slicing misto
print(arr_2d[1:3, 1:3]) # Output: [[6 7 ]
                        #         [10 11]]
