class Computer:
    def __init__(self, processore):
        self.__processore = processore # attributo privato
    def get_processore(self):
        return self.__processore
    def set_processore(self, processore):
        self.__processore = processore
        
c = Computer("Intel Ultra 7")
print(c.get_processore())
c.set_processore("AMD RYZEN 7")
print(c.get_processore())
c.__processore = "AMD RYZEN 5"
print(c.get_processore()) # Stampa ancora "AMD RYZEN 7"
print(c.__processore)     # Stampa "AMD RYZEN 5"

# Quando scrivi c.__processore = ... dall'esterno, Python non sta modificando l'attributo privato vero. 
# Sta creando un nuovo attributo volante che si chiama casualmente nello stesso modo.
# L'attributo privato vero è ancora al sicuro dentro la classe, protetto dal "muro" che hai costruito.
# Anche i metodo possono essere definiti privati e protetti ("fingendo" di usarli solo interno classe)
# def __smonta():
#   print("computer smontato")

# PROPERTY
class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.__voto = voto
    @property # detta annotazione, definisco una funzione come il getter di voto
    def voto(self):
        print("Voto getter")
        return self.__voto
    @voto.setter # metodo che controlla come viene modificato il valore dell’attributo. (usato per validazione/controlli sui dati)
    def voto(self, nuovo_voto):
        if(0 <= nuovo_voto <= 30):
            self.voto = nuovo_voto
        else:
            print("voto non valido")   

s = Studente("Emy", 8)
print(s.voto) # richiamiamo come se fosse un attributo/variabile grazie a property, che rende più facile il richiamo
              # sostituendo anche a livello di scrittura self.__voto (una funzione che ha lo stesso nome della variabile privata, usando quella)
s.voto = -5
s.voto = 30
print(s.voto)