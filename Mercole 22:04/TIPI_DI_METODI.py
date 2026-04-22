# I METODI

# tipi di metodi:
# metodi di istanza - metodi di classi - metodi statici

# ESEMPIO METODO STATICO:

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b
    
risultato = Calcolatrice.somma(2, 10)
print(risultato)

# CLASSMETHOD - legato alla classe

class Contatore:
    numero_istanze = 0
    def __init__(self):
        Contatore.numero_istanze += 1
    @classmethod
    def mostra_numero_istanze(cls): 
        print(f"Sono state create {cls.numero_istanze}")
c1 = Contatore
c2 = Contatore
Contatore.mostra_numero_istanze()

# Altro Esempio

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    @classmethod
    def init_from_string(cls, s: str): # nel caso in cui riceva informazioni da csv per esempio
        nome, età = s.split(",") # stringa in arrivo "Mario, 30"
        return cls(nome, int(età))
    
p = Persona.init_from_string("Mario, 30")
print(p.nome, p.età)

        