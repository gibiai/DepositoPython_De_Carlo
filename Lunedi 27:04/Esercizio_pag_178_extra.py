import random

class MetodoPagamento:
    def __init__(self, tasso_interesse): # ogni metodo ha il suo tasso di interesse
        self.tasso_interesse = tasso_interesse # salvato come attributo

    def effettua_pagamento(self, importo):
        pass

class CartaDiCredito(MetodoPagamento):
    def __init__(self):
        super().__init__(0.05) # 5% di interesse

    def effettua_pagamento(self, importo):
        totale = importo + (importo * self.tasso_interesse) # calcola importo + interesse
        print(f"Pagamento di {importo}€ + {self.tasso_interesse*100}% interesse = {totale:.2f}€ con Carta di Credito")
        return totale # restituisce il totale per scalarlo dal credito

class Paypal(MetodoPagamento):
    def __init__(self):
        super().__init__(0.03) # 3% di interesse

    def effettua_pagamento(self, importo):
        totale = importo + (importo * self.tasso_interesse)
        print(f"Pagamento di {importo}€ + {self.tasso_interesse*100}% interesse = {totale:.2f}€ con PayPal")
        return totale

class BonificoBancario(MetodoPagamento):
    def __init__(self):
        super().__init__(0.01) # 1% di interesse

    def effettua_pagamento(self, importo):
        totale = importo + (importo * self.tasso_interesse)
        print(f"Pagamento di {importo}€ + {self.tasso_interesse*100}% interesse = {totale:.2f}€ con Bonifico Bancario")
        return totale

class GestorePagamenti:
    def __init__(self, metodo):
        self.__metodo = metodo

    def paga(self, importo):
        return self.__metodo.effettua_pagamento(importo) # restituisce il totale

class Utente:
    def __init__(self, nome):
        self.__nome = nome
        self.__credito = random.randint(1, 100)
        print(f"Benvenuto {self.__nome}! Il tuo credito è {self.__credito}€")

    def scegli_pagamento(self):
        print("\nScegli metodo di pagamento:")
        print("1 - Carta di Credito (5% interesse)")
        print("2 - PayPal (3% interesse)")
        print("3 - Bonifico Bancario (1% interesse)")

        scelta = input("Scelta: ")
        importo = int(input("Importo da pagare: "))

        match scelta:
            case "1":
                metodo = CartaDiCredito()
            case "2":
                metodo = Paypal()
            case "3":
                metodo = BonificoBancario()
            case _:
                print("Scelta non valida!")
                return

        totale = importo + (importo * metodo.tasso_interesse) # calcola totale con interesse

        if totale > self.__credito: # blocca se il totale supera il credito
            print(f"Credito insufficiente! Il totale con interesse sarebbe {totale:.2f}€")
            return

        gestore = GestorePagamenti(metodo)
        self.__credito -= gestore.paga(importo) # scala il totale dal credito
        print(f"Credito rimanente: {self.__credito:.2f}€")

# TEST
utente = Utente("Mario")
utente.scegli_pagamento()