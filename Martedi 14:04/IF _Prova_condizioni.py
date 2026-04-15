numero = 10
if numero > 0:
    print("Il numero è positivo")
    
numero = -1
if numero > 0:
    print("il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("il numero è negativo")

else:
    print("il numero è zero")
    

# Test match

comando = input("inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")