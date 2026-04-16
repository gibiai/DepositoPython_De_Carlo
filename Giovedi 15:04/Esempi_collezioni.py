# TUPLE
# usate per raggruppare valori correlati o per rappresentare
# una sola entità (es: coordinate piano cartesiano)

punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpacking 
print(x, y) # Output: 3 4

# INSIEMI
# tipo sets: strutture dati specializzate in non avere duplicati

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}
