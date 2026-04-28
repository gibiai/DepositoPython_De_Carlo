from abc import ABC, abstractmethod

class Animale(ABC): # classe vuota astratta che non è istanziata
    @abstractmethod # decoratore 
    def muovi(self): # metodo che le altre classi erediteranno
        pass

class Cane(Animale): # classe che eredita il metodo astratto
    def muovi(self):
        print("Corro") # differenza di azione per questa classe

class Pesce(Animale):
    def muovi(self):
        print("Nuoto")
        