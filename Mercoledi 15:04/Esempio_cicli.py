# While ripetizione ciclica numerica di un blocco di codice
# finchè una determinata condizione è vera
# ogni iterazione prima verificata, se true l'iterazione continua
# ciclo ripete fino a che l’elemento conteggio sarà inferiore a 5

conteggio = 0

while conteggio < 5:
    print(conteggio)
    conteggio += 1 

# Ciclo davvero utile non è il numerico ma quello Booleano

controllore = False

while controllore:
    print("ciao")
    scelta = input("vuoi continuare?").lower()
    if scelta == "no":
        controllore = False 

# For si usa quando posso determinare quante ripetizioni voglio fare
# While quando non posso sapere quante ripetizioni farà l'utente
# For cicli determinabili
# While non determinabili o che non voglio determinare

# For ripete x volte un elemento / ciclare in una sequenza
# Esempio:

numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    print(numero) 

# Range - funzione (incorporata) aggiuntiva o ausiliare per il For
# parte obbligatoria Stop / Start e Step sono opzionali
# comportamento funzionale che si occupa di eseguire una sequenza
# di numeri interi in cicli for o altre situazioni, itera un insieme di valori

# Esempio 1:

for i in range(5):
    print(i)

# Esempio 2:

for i in range(2, 8):
    print(i)

# Esempio con Start Stop Step:

for i in range(1, 10, 2):
    print(i)


