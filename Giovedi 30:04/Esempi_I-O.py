# Apertura di un file in modalità scrittura e scrittura di alcune righe

file = open("prova1.txt", "w") # apertura del file in modalità scrittura
file.write("Ciao, questo è un file di prova.\n") # scrittura di una riga nel file
file.write("Questa è la seconda riga del file.\n") # scrittura di un'altra riga nel file
file.close() # chiusura del file


# uso with open per gestire i file in modo sicuro e automatico

with open("prova1.txt", "r") as file: # apertura del file in modalità lettura
    contenuto = file.read() # lettura del contenuto del file
    print(contenuto) # stampa del contenuto del file
    
    
# esempi imput e output

file = open("prova1.txt", "r") # apertura del file in modalità lettura
contenuto = file.read() # lettura del contenuto del file
riga = file.readline() # lettura di una riga del file
print(contenuto) # stampa del contenuto del file
print(riga) # stampa della riga letta
file.close() # chiusura del file 