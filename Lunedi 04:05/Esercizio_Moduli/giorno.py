# Modulo gestione data

from abc import ABC, abstractmethod # importo ABC per classi astratte

class GiornoBase(ABC): # classe astratta - definisce la struttura base di un giorno
    def __init__(self, data, vendite):
        self._data = data # data del giorno protetta
        self._vendite = vendite # lista vendite del giorno protetta

    @property # al posto di get_data() / imposto solo lettura sui dati - protegge dati
    def data(self):
        return self._data

    @property # sostituisce get_vendite / permette uso come attributo e non metodo
    def vendite(self):
        return self._vendite

    @abstractmethod # ogni sottoclasse deve implementarlo !!!
    def descrizione(self): # metodo astratto - descrizione del giorno
        pass


class Giorno(GiornoBase): # classe concreta che eredita da GiornoBase
    def __init__(self, data, vendite):
        super().__init__(data, vendite) # chiama costruttore classe madre

    def totale(self): # calcola il totale delle vendite del giorno
        return sum(self._vendite)

    def media(self): # calcola la media delle vendite del giorno
        if len(self._vendite) == 0: # check che non sia vuota
            return 0
        return sum(self._vendite) / len(self._vendite)

    def descrizione(self): # implementazione metodo astratto che descriva il giorno
        return f"Giorno {self._data} | Vendite: {self._vendite} | Totale: {self.totale():.2f}€ | Media: {self.media():.2f}€"