# Esempio di simulazione Overloading, utilizzando argomenti opzionali o variadici
# Overloading : possibilità di avere più metodi nella stessa classe con lo stesso 
# nome, ma con differenti parametri. Non è supportato direttamente in Python
class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
