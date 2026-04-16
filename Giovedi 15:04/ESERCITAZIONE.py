import random

# FUNZIONE 1 - validazione e generazione della lista

def genera_lista(): # chiede numero positivo e genera la lista casuale
    n = int(input("Inserisci un numero intero positivo: "))
    while n <= 0: # continua a chiedere fino a quanto non è positivo
        print("Numero non valido!")
        n = int(input("Inserire numero positivo: "))
    lista = []
    for i in range(n): # genera numeri casuali tra 1 e n
        lista.append(random.randint(1, n))
    print("Lista generata:", lista)
    return lista # restituisce la lista per usarla nelle altre def

# FUNZIONE 2 - Somma pari

def somma_pari(lista): # calcola la somma dei numeri pari nella lista
    somma = 0
    for numero in lista:
        if numero % 2 == 0: # controlla se il numero è pari
            somma += numero # aggiunge il numero alla somma
    print("Somma dei pari:", somma)

# FUNZIONE 3 - Stampa dispari

def stampa_dispari(lista): # stampa tutti i numeri dispari nella lista
    for numero in lista:
        if numero % 2 != 0: # controlla se il numero è dispari
            print(numero)

# FUNZIONE 4 - Controlla se è numero primo

def primo_t(numero): # controlla se numero è primo, così restituisce True
    if numero <= 1: # controllo per evitare 0 e 1, non sono numeri primi
        return False
    for i in range(2, numero): # controlla se è divisbile tra '2' e 'n'
        if numero % i == 0: # se il resto è 0 non è primo
            return False
    return True # se non trova valori allora è primo

# FUNZIONE 5 - Stampa tutti i primi nella lista

def stampa_primi(lista):
    for numero in lista:
        if primo_t(numero): # controllo che richiama funzione primo_t su ogni numero
            print(numero)

# FUNZIONE 6 - Controlla se la somma è prima

def controllo_somma_prima(lista): # controlla se la somma di tutti i numeri lista è prima
    somma = 0
    for numero in lista:
        somma += numero # somma tutti i numeri della lista
    if primo_t(somma): # richiama primo_t sulla somma totale
        print("La somma", somma, "è un numero primo")
    else:
        print("La somma", somma, "non è un numero primo")

# FUNZIONE 0 - MENU

def view_menu(): # creiamo menu per la scelta dell'utente
    print("\n---- Menu ----")
    print("1. Genera lista")
    print("2. Somma pari")
    print("3. Stampa dispari")
    print("4. stampa primi")
    print("5. Verifica se la somma è prima")
    print("0. Esci")

# FUNZIONE MAIN - funzione principale che gestisce menu e flusso del programma

def main():
    lista = [] # lista vuota iniziale, viene riempita con il punto 1
    
    while True:
        view_menu() # stampa sempre menu ogni giro
        scelta = input("Scegli un'opzione: ")
        
        match scelta:
            case "1":
                lista = genera_lista() # inizializza la lista e la salva
            case "2":
                if not lista: # ferma l'esecuzione se la lista non esite
                    print("Devi prima generare la lista con il punto 1!")
                else:
                    somma_pari(lista) # calcola e stampa la somma dei numeri pari presenti
            case "3":
                if not lista: # se lista vuota non si può procedere
                    print("Devi prima generare la lista con il punto 1!")
                else:
                    stampa_dispari(lista) # stampiamo tutti i numeri dispari della lista
            case "4":
                if not lista: # altro check che evita operazioni se lista vuota
                    print("Devi prima generare la lista con il punto 1!")
                else:
                    stampa_primi(lista) # stampa i numeri primi presenti nella lista
            case "5":
                if not lista: # altro controllo sulla presenza dei dati
                    print("Devi prima generare la lista con il punto 1")
                else:
                    controllo_somma_prima(lista) # esegue controllo sulla somma (logica definita nella funzione)
            case "0":
                print("Alla prossima!") 
                break # esce dal while True e termina il programma
            case _: #  gestione input non valido 
                print("Mi dispiace, scelta non valida")
        
# avviare il programma: 
# main() 