# modulo per la gestione delle classi
# gestisce la gerarchia dei piatti del nostro ristorante
from abc import ABC, abstractmethod # importo libreria

# classe base astratta come modello per le sottoclassi
class Piatto(ABC):
    # disponibile=True come default: non rompe le sottoclassi già scritte
    def __init__(self, codice, nome, categoria, prezzo, disponibile=True):
        self.codice      = codice
        self.nome        = nome
        self.categoria   = categoria
        self.__prezzo    = prezzo       # unico attributo privato - accedo con property
        self.disponibile = disponibile  # booleano: True = in menu, False = esaurito

    @property
    def prezzo(self): # permette di leggere prezzo come attributo normale
        return self.__prezzo

    @prezzo.setter # setter: permette modifica __prezzo solo se valore positivo
    def prezzo(self, valore):
        if valore > 0: # validazione: prezzo non può essere negativo
            self.__prezzo = valore
        else:
            print("Il prezzo deve essere maggiore di zero!")

    @abstractmethod # metodo astratto per ogni sottoclasse
    def descrivi(self):
        pass

    @abstractmethod
    def get_tipo(self): # ogni sottoclasse restituisce il suo tipo
        pass

    def to_dict(self): # salva in un dizionario tutti i dati dei piatti, in file_manager scrive csv
        return {
            "codice":       self.codice,
            "nome":         self.nome,
            "categoria":    self.categoria,
            "prezzo":       self.prezzo,
            "tipo":         self.get_tipo() # polimorfico, ogni classe risponde col suo tipo
        }

    def __str__(self): # metodo speciale - restituisce stringa leggibile con stato disponibilità
        # mostra il simbolo di disponibilità direttamente nella rappresentazione testuale
        stato = "✅" if self.disponibile else "❌"
        return f"[{self.codice}] {self.get_tipo().upper()} - {self.nome} | €{self.prezzo:.2f} | {stato}"


class Antipasto(Piatto):
    def __init__(self, codice, nome, categoria, prezzo, porzione):
        super().__init__(codice, nome, categoria, prezzo)
        self.porzione = porzione # attributo specifico antipasti

    # implementazione obbligatoria del metodo astratto descrivi()
    def descrivi(self):
        stato = "✅ Disponibile" if self.disponibile else "❌ Esaurito"
        print(f"[{self.codice}] ANTIPASTO - {self.nome} | €{self.prezzo:.2f} | {stato}")
        print(f"  → Porzione: {self.porzione}")

    # implementazione obbligatoria del metodo astratto get_tipo()
    def get_tipo(self):
        return "Antipasto"


# sottoclasse Primo: eredita da Piatto e aggiunge l'attributo specifico tipo_pasta
class Primo(Piatto):

    def __init__(self, codice, nome, categoria, prezzo, tipo_pasta):
        super().__init__(codice, nome, categoria, prezzo)
        # attributo specifico dei primi piatti
        self.tipo_pasta = tipo_pasta

    def descrivi(self):
        stato = "✅ Disponibile" if self.disponibile else "❌ Esaurito"
        print(f"[{self.codice}] PRIMO - {self.nome} | €{self.prezzo:.2f} | {stato}")
        print(f"  → Tipo pasta: {self.tipo_pasta}")

    def get_tipo(self):
        return "Primo"


# sottoclasse Secondo: eredita da Piatto e aggiunge l'attributo specifico cottura
class Secondo(Piatto):

    def __init__(self, codice, nome, categoria, prezzo, cottura):
        super().__init__(codice, nome, categoria, prezzo)
        # attributo specifico dei secondi piatti
        self.cottura = cottura

    def descrivi(self):
        stato = "✅ Disponibile" if self.disponibile else "❌ Esaurito"
        print(f"[{self.codice}] SECONDO - {self.nome} | €{self.prezzo:.2f} | {stato}")
        print(f"  → Cottura: {self.cottura}")

    def get_tipo(self):
        return "Secondo"