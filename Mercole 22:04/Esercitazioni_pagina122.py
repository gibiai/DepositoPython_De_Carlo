#ESERCIZIO STATICMETHOD 
class Convertitore:
    
    @staticmethod # decoratore statico quindi non accede all'interno serve solo input
    def euro_in_dollari(importo): # metodo statico quindi niente self, chiamo direttamente
        return importo * 1.08 # tasso di cambio
    
    @staticmethod
    def km_in_miglia(km): 
        return km * 0.621371 # tasso di cambio 
    
# TEST - senza creare oggetti
euro = float(input("Inserisci importo in euro: "))
print("In dollari equivale a:", Convertitore.euro_in_dollari(euro)) # chiamo funzione direttamente dal nome della classe
                                                                    # evitando istanza
km = float(input("Inserisci distanza in km: "))
print("In miglia equivale a:", Convertitore.km_in_miglia(km))

# ESERCIZIO CLASSMETHOD
class Animale:
    numero_animali = 0 # attributo di classe come da traccia inizializzato a 0
    def __init__(self, nome, specie): # costruttore
        self.nome = nome # attributo di istanza
        self.specie = specie # attributo di istanza
        Animale.numero_animali += 1 # incrementa il contatore ogni volta che si crea animale

    @classmethod # decoratore che indica che il metodo lavora con la classe stessa
    def quanti_animali(cls): # cls è la classe stessa, come self ma per i classmethod e legge contatore condiviso da tutti
        print("Numero di animali creati:", cls.numero_animali)      
# TEST - creiamo 3 animali
a1 = Animale(input("Nome animale 1: "), input("Specie animale 1: "))
a2 = Animale(input("Nome animale 2: "), input("Specie animale 2: "))
a3 = Animale(input("Nome animale 3: "), input("Specie animale 3: "))

Animale.quanti_animali()  # chiamato dalla classe, come da traccia