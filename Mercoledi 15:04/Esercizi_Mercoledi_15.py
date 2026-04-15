# ESERCIZIO 1
eta = int(input("Inserisci la tua età: ")) # converte l'input in un numero intero

if eta < 18:
    print("Mi dispiace, non puoi vedere il film.")
else:
    print("Puoi vedere questo film!")
    
# ESERCIZIO 2
num1 = int(input("Primo numero: ")) 
num2 = int(input("Secondo numero: "))
operazione = input("Operazione (+, -, *, /): ")

match operazione:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0: #controllo la divisione per 0
            print("Errore: divisione per 0")
        else:
            print(num1 / num2)
    case _:
        print("Operazione non valida!")
        
# ESERCIZIO 1 - Conto alla rovescia:

numero = int(input("Inserisci un numero: "))
for i in range(numero, -1, -1): # parte dal numero e scende fino a 0
    print(i)
ripeti = input("Vuoi ripetere? (S/N): ")
if ripeti == "S":
    for i in range(numero, -1, -1):
        print(i)

# ESERCIZIO 2 - Numeri primi

primi = [] # lista dove salviamo input
while len(primi) < 5: # entro nel cilo e conto la lunghezza, eseguendolo fino ad avere 5 numeri primi nella lista
    numero = int(input("Inserisci un numero: "))
    scelta = input("P = primo, A = pari: ") # scelta utente sul controllo del tipo numero
    if scelta == "A":
        if numero % 2 == 0: # operatore modulo per controllo numero pari, verifico se resto uguale a 0
            print("Il numero è pari")
        else:
            print("Il numero non è pari")
    else:
        if numero > 1 and numero % 2 != 0: # check se numero primo:  > 1 & !/ 2 - SE entrambe vere
            primi.append(numero) # aggiungiamo il numero alla lista 
            print("Il numero è primo")
        else:
            print("Il numero non è primo")