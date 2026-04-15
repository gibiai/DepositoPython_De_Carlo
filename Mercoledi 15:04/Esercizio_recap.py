# ESERCIZIO COMPLETO
#
# Punto 1 - while per garantire numero positivo
#
n = int(input("Inserire un numero positivo: "))
while n <= 0: # continua a richiedere un input positivo all'utente
    print("Numero non valido! Riprova.")
    n = int(input("Ripeti l'inserimento del numero positivo: "))
#
# MENU - utente sceglie cosa fare
#
scelta = input("1 = somma pari, 2 = dispari, 3 = controlla primo: ") 
if scelta == "1":
    somma = 0 # variabile che accumula somma
    for i in range(1, n + 1): # scorre da 1 a n INCLUSO
        if i % 2 == 0: # check se numero pari
            somma += i # continuo iterazione, aggiungendo numero alla somma
    print("Somma dei pari:", somma) # stampa la somma di tutti i numeri pari compresi
elif scelta == "2":
    for i in range(1, n + 1): # scorre da 1 a n INCLUSO
        if i % 2 != 0: # check se numero dispari
            print(i) # stampa solo numeri dispari, con resto diverso da 0
elif scelta == "3": 
    primo_t = True # presumiamo che sia primo
    for i in range(2, n): # controlla se n è divisibile per qualcosa tra 2 e n
        if n % i == 0: # se il resto è 0 non è primo
            primo_t = False # cambiamo lo status in base al resto
    if primo_t and n > 1:
        print(n, "è numero primo")
    else:
        print(n, "non è numero primo")
else:
    print("Scelta non valida")
