# CLASSI - OOP 
# specifica entità che stiamo gestendo (es: garage auto, o utente, supermercado -> magazzino etc etc)
# queste sono dette classi o oggetti - tramite variabili e funzioni
# attributi definiscono caratteristiche (utente = nome, cognome , età etc etc)
# metodi/funzioni definiscono il suo comportamento (utente esempio acquista, si iscrive ...)
# l'oggetto è l'istanza - identiche alla classe ma ognuna ha vita propria 
# (può essere creato e distrutto senza operare sulla classe)
# crei progetto -> istanzi più volte quel progetto.

# Classi: astrazioni dei concetti reali - modello per creare oggetti
# definita con "class"
# attributi sono variabili associate ad una classe
# di classe sono condivisi con tutte le istanze

# Metodi: sono funzioni associate alla classe
# rappresentano il comportamento di un oggetto

# ESEMPIO :
class Automobile: # dichiaro la classe
    numero_ruote_ = 4 # attributo di classe
    def __init__(self, marca, modello): # metodo costruttore, sempre __init__ più i parametri da inizializzare / posso fare marca : str / modello : str
        self.marca = marca # attributo di istanza / uguale alla dichiarazione e inizializzazione di una variabile
        self.modello = modello # attributo di istanza
    def stampa_info(self): # metodo di istanza che fa riferimento all'oggetto
        print("L'automobile è una", self.marca, self.modello) # 
        # print(f"L'automobile è una {self.marca} {self.modello}") / altro modo di printare

auto1 = Automobile("Fiat", "500") # crea un oggetto di Automobile
auto2 = Automobile("BMW", "X3") # crea un altro oggetto di Automobile

# auto1.marca = "Mercedes"
# auto1.modello = "Classe E" posso cambiare in qualsiasi modello 

# auto1.numero_ruote = 6 / ma auto2 ancora con 4 ruote, non subisce cambiamento // Automobile.numero_ruote = 8 , questo per tutti
# print(f"numero ruote: {auto1.numero_ruote}")

auto1.stampa_info() # stampa = "L'automobile è una Fiat 500"
auto2.stampa_info() # stampa = "L'automobile è una BMW X3"

# __init__ costruttore, metodo speciale invocato automaticamente alla creazione di un oggetto

# Metodi:
# metodi di istanza operano sui dati dell'oggetto self
# metodi di classe operano non sull'istanza specifica, definiti con decoratore @ e ricevono come primo parametro la classe @classmethod
# metodi statici legati alla classe ma non operano ne' su quest'ultima ne sull'istanza, definiti con decoratore @staticmethod

# ESEMPIO:

import Automobile as Auto

def crea_auto(marca: str, modello: str):
    auto = Auto.Automobile(marca, modello)
    auto.stampa_info()

def main():
    lista_auto = []
    while True:
        marca = input("Inserisci la marca (Q per uscire): ")
        if marca.lower() == "q":
            break
        modello = input("Inserisci modello: ")
        nuova_auto = Auto.Automobile(marca, modello)
        lista_auto.append(Auto.Automobile(marca, modello))

    print(f"\n Auto in lista: {len(lista_auto)}")
    for auto in lista_auto:
        auto.stampa_info()
        
if __name__ == "__main__":
   main() 