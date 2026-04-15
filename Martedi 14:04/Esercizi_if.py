# PRIMO ESERCIZIO:

x = int(input("definisci x: "))  # converte l'input in numero intero
if x > 0:
    print("x è positivo")
    if x > 10:
        print("x maggiore di 10")
        if x == 100:
            print(" x è 100")
            
                      
# SECONDO ESERCIZIO:

numeri = []  # lista vuota dove salviamo i numeri
scelta = input("C = aggiungi, U = modifica, D = elimina, V = visualizza: ")
if scelta == "C":
    numeri.append(int(input("Numero: ")))  # aggiunge il numero in fondo alla lista
    print(numeri)
elif scelta == "U":
    numeri[0] = int(input("Nuovo numero: "))  # modifica il primo elemento della lista
    print(numeri)
elif scelta == "D":
    numeri.remove(int(input("Numero da eliminare: ")))  # rimuove il numero dalla lista
    print(numeri)
elif scelta == "V":
    print(numeri)
else:
    print("Errore")

# TERZO ESERCIZIO:

utenti = []  # lista vuota dove salviamo gli utenti
id_counter = 1  # id parte da 1 e cresce ad ogni registrazione
scelta = input("R = registrati, L = accedi: ")
if scelta == "R":
    nome = input("Nome: ")
    password = input("Password: ")
    utenti.append([id_counter, nome, password])  # salva id, nome e password insieme
    id_counter += 1  # incrementa l'id per il prossimo utente
    print(utenti)
else:
    nome = input("Nome: ")
    password = input("Password: ")
    if [utenti[0][1], utenti[0][2]] == [nome, password]:  # controlla nome e password utente
        print("Accesso effettuato")
        print("Il tuo id è:", utenti[0][0])
    else:
        print("Account non trovato")