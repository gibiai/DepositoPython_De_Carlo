import random # importo libreria per generare numeri random

class MetodoPagamento: # classe "vuota"
    def effettua_pagamento(self, importo): # metodo base da implementare sottoclassi
        pass # placeholder

class CartaDiCredito(MetodoPagamento): # eredita da MetodoPagamento
    def effettua_pagamento(self, importo): # override - simula pagamento con carta
        print(f"Pagamento di {importo}€ effettuato con carta di credito")

class Paypal(MetodoPagamento): # eredita sempre da MetodoPagamento
    def effettua_pagamento(self, importo): # override - simula pagamento con carta
        print(f"Pagamento di {importo}€ effettuato con Paypal")

class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self, importo): # override - paga con bonifico
        print(f"Pagamento di {importo}€ effettuato con bonifico bancario")
        
class GestorePagamenti:
    def __init__(self, metodo): # riceve qualsiasi metodo di pagamento
        self.__metodo = metodo # salva il metodo scelto e lo rende privato
    
    def paga(self, importo): # richiama effettua_pagamento senza sapere quale metodo ancora
        self.__metodo.effettua_pagamento(importo)

class Utente:
    def __init__(self, nome):
        self.__nome = nome # nome utente privato
        self.__credito = random.randint(1, 100) # genero credito casuale tra 1 e 100
        print(f"Benvenuto {self.__nome}! Il tuo credito è {self.__credito}€")

    def scegli_pagamento(self):
        print("\nScegli metodo di pagamento:")
        print("1 - Carta di Credito")
        print("2 - Paypal")
        print("3 - Bonifico Bancario")
    
        scelta = input("Scelta: ") # legge scelta dell'utente
        importo = int(input("Importo da pagare: ")) # converte input in int
        
        if importo > self.__credito: # controlla e blocca in caso non ha abbastanza credito
            print("credito insufficiente") 
            return # esce dal ciclo senza fare nulla
        
        match scelta: # controlla il valore di scelta
            case "1":
                metodo = CartaDiCredito()  
            case "2":
                metodo = Paypal()  
            case "3":
                metodo = BonificoBancario()
            case _:
                print("Scelta non valida!")
                return # esce dal metodo

        gestore = GestorePagamenti(metodo) # crea il gestore con metodo scelto
        gestore.paga(importo) # effettua il pagamento tramite il gestore
        self.__credito -= importo # sottrae l'importo dal credito
        print(f"Credito rimanente: {self.__credito}€")

# TEST
utente = Utente("Mario") # crea utente con credito casuale
utente.scegli_pagamento() # avvia la scelta del pagamento
