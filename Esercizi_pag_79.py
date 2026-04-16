# PUNTO 1 - Pari o Dispari

numeri = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")

# PUNTO 2 - Conto alla rovescia con ripetizione infinita

while True:
    n = int(input("Inserisci un numero positivo: "))
    
    for i in range(n, -1, -1): # scorre da n fino a 0 incluso
        print(i)
        
    ripeti = input("Vuoi ripetere? (S/N): ")
    if ripeti != "S":
        break # esce dal ciclo

# PUNTO 3 - Quadrato di ogni numero nella lista

numeri = []
n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n): # chiede n numeri e li salva nella lista
    numeri.append(int(input("Inserisci un numero: ")))
for numero in numeri: # scorre la lista e stampa il quadrato
    print(numero, "al quadrato è", numero ** 2)
    
# PUNTO 4 - Massimo, contatore e lista vuota

numeri = []
n = int(input("Quanti numeri vuoi inserire? "))

for i in range(n): # chiede n numeri e li salva nella lista
    numeri.append(int(input("Inserisci un numero: ")))
if len(numeri) == 0: # controlla se la lista è vuota
    print("Lista vuota")
else:
    massimo = numeri[0] # partiamo dal primo elemento come massimo
    for numero in numeri:
        if numero > massimo: # se troviamo un numero più grande lo sostituiamo
            massimo = numero
    contatore = 0 # conta quanti numeri ci sono nella lista
    while contatore < len(numeri):
        contatore += 1
        
    print("Numero massimo:", massimo)
    print("Numero di elementi:", contatore)
    