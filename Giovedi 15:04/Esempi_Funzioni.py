# FUNZIONI

# Esempio senza return

def saluta(nome):
    print("Ciao,", nome)

def somma(a, b):
    risultato = a + b
    print("La somma è:", risultato)
    
# Richiamo Funzioni (sopra solo definite)

saluta("Alice") # Output: Ciao, Alice
somma(5, 3) # Output: la somma è: 8

# Esempio con return
# (sempre singolo se codice non condizionato)



# Esempio Funzioni Generatori
# permettono iterare su una di valori, ma uno alla volta
# utile per grandi sequenze
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a # transforma parola chiave in "generatore"
        a, b = b, a + b

# Esempio Funzioni Decoratori

# TEORIA

def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

# PRATICA

@decoratore
def saluta():
    print("Ciao!")

saluta()