# ESERCIZI FUNZIONI

# 1 Esercizio Base - Indovina il numero

import random  # libreria per generare numeri casuali

def indovina_numero():
    numero_segreto = random.randint(1, 100)  # genera un numero casuale tra 1 e 100

    while True: # ciclo madre - mostra menu iniziale
        scelta = input("G = gioca, U = esci: ") # menu azioni utente

        if scelta == "G": # scelta per entrare nel ciclo interno 
            while True:  # loop interno solo per gestire il gioco e la resa
                tentativo = int(input("Inserisci un numero tra 1 e 100: ")) # scelta numero
                
                if tentativo == numero_segreto:
                    print("Hai indovinato!")
                    break # in caso coincida la scelta esce dal loop interno
                elif tentativo < numero_segreto:
                    print("Più alto!")
                else:
                    print("Più basso!")
                
                resa = input("Ti arrendi? (S/N): ") # scelta dopo ogni tentativo
                if resa == "S": # rivela il numero se utente sceglie la resa
                    print("Il numero era:", numero_segreto)
                    break
            break  # esce dal while esterno dopo la partita
        
        elif scelta == "U":
            print("Hai deciso di uscire, il numero era:", numero_segreto)
            break

# 2 Esercizio Avanzato - Sequenza di Fibonacci fino a N
# (Fibonacci = ogni numero è la somma dei due precedenti)

def Fibonacci():
    n = int(input("Inserisci un numero: "))
    a = 0 # primo numero della sequenza (Fibonacci parte sempre da zero)
    b = 1 # secondo numero della sequenza (0,1 sempre primi due numeri fissi)

    while a <= n: # ciclo continua a stampare finchè a quando 'a' non supera 'n'
        print(a)
        temp = a # memorizzo stato attuale 'a' nel ciclo
        a = b # successivamente 'a' diventa 'b'
        b = temp + b # 'b' diventa la somma dei due precedenti 
        # || a, b = b, a + b / assegnamento multiplo
        
# Chiamata funzioni:
# indovina_numero()
# Fibonacci()