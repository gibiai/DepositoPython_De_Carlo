# ESERCIZIO 1 - Pari/Dispari con ripetizione

while True: # esegue all'infinito a scapito dell'utente
    scelta = input("N = numero, S = stringa: ")
    
    if scelta == "N":
        numero = int(input("Inserisci un numero: "))
        if numero % 2 == 0:
            print("Pari")
        else:
            print("Dispari")
    elif scelta == "S":
        stringa = input("inserisci una stringa: ")
        if len(stringa) % 2 == 0: # controlla se lunghezza str è pari
            print("La stringa ha un numero di lettere pari")
        else:
            print("La stringa ha un numero di lettere dispari")
            
    ripeti = input("Vuoi ripetere? (S/N): ")
    if ripeti != "S": # se non vuole ripetere esce dal while
        break
    
# ESERCIZIO 2 - Numeri primi in un intervallo

while True: # gira all'infinito finchè l'utente non sceglie di fermarsi
    n1 = int(input("inserisci il primo numero dell'intervallo: "))
    n2 = int(input("inserisci il secondo numero dell'intervallo: "))
    
    primi = [] # lista per numeri primi
    non_primi = [] # lista per numeri non primi
    
    for i in range(n1, n2 + 1): # scorre tutti i numeri nell'intervallo
        primo_t = True # assumiamo che sia un numero primo 
        for j in range(2, i): # scorriamo i numeri nell'intervallo
            if i % j == 0: # verifica se divisibile per 2 o numero stesso
                primo_t = False # se lo è non è primo
        if primo_t and i > 1: # se condizioni vere e quindi numero primo, lo aggiungiamo
            primi.append(i)
        else:
            non_primi.append(i)
    
    scelta = input("P = primi, N = non primi, E = entrambi: ") # menu scelte utente dopo aver trovato tutti i numeri
    
    if scelta == "P":
        print("Numeri primi:", primi)
    elif scelta == "N":
        print("Numeri non primi:", non_primi) 
    elif scelta == "E":
        print("Numeri primi", primi)
        print("Numeri non primi", non_primi)
    
    ripeti = input("Vuoi ripetere? (S/N): ")
    if ripeti != "S":
        break # usciamo dal while se l'utente lo seleziona

# ESERCIZIO 3 - Fattori comuni e stringhe complementari

while True: # condizione per far sempre girare all'infinito in base all'utente
    scelta = input("N = numeri, S = stringhe: ")
    
    if scelta == "N":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        
        fattori = [] # lista dove salviamo
        for i in range(2, min(n1, n2) +1): # scorre fino al più piccolo dei due
            if n1 % i == 0 and n2 % i == 0: # controlla se divide entrambi
                fattori.append(i)
        if len(fattori) == 0: # se la lista è vuota non ci sono fattori comuni
            print("I numeri sono comprimi")
        else:
            print("Fattori comunu:", fattori)
    elif scelta == "S":
        s1 = input("inserisci la mia prima stringa: ")
        s2 = input("Inserisci la seconda stringa: ")
        
        lettere_comuni = [] # lista dove salviamo le lettere comuni
        for lettera in s1:
            if lettera in s2 and lettera not in lettere_comuni: # evita duplicati
                lettere_comuni.append(lettera)
        if sorted(s1) == sorted(s2):  # stesse lettere in ordine diverso?
            print("Le stringhe sono complementari")
        elif len(lettere_comuni) == 0:
            print("Nessuna lettera in comune")
        else:
            print("Lettere comuni:", lettere_comuni)

    ripeti = input("Vuoi ripetere? (S/N): ")
    if ripeti != "S":
        break