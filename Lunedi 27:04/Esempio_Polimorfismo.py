# Primo Esempio
class origine():# Classe madre (Astrazione): definisce l'idea generica di lavoratore   def lavoro(self):
        pass

class lavoratore_manuale(origine): # Sottoclasse che eredita da origine (Ereditarietà)
    def lavoro(self):
        print("Sto lavorando con le mani: Costruisco un muro.")

class lavoratore_digitale(origine): # Altra sottoclasse che eredita da origine
    def lavoro(self):
        print("Sto lavorando con il computer: Scrivo codice Python.")

# Non le importa SE è manuale o digitale, le basta che sappia fare .lavoro()
def fai_lavorare(lavoratore: origine): # Funzione Polimorfica: accetta un qualsiasi oggetto di tipo 'origine'
    lavoratore.lavoro()

# Secondo esempio
class Cerchio: 
    def disegna(self):
        print("Disegno un cerchio")

class Rettangolo:
    def disegna(self):
        print("Disegno un rettangolo")

def disegna_figura(figura): # Anche qui, basta che 'figura' abbia il medoto 'disegna'
    figura.disegna()

figure = [Cerchio(), Rettangolo()] # figure[0] = Cerchio() / figure[1] = Rettangolo()

for figura in figure: # Iteriamo e disegniamo ogni figura
    disegna_figura(figura)