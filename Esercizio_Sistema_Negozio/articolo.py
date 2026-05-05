# Modulo gestione singolo articolo inventario

class Articolo: # classe per rappresentare un articolo in inventario
    def __init__(self, nome, prezzo, quantità):
        self.__nome = nome # nome articolo privato
        self.__prezzo = prezzo # prezzo articolo privato
        self.__quantità = quantità # quantità disponibile privata
        
    @property # getter nome
    def nome(self):
        return self.__nome

    @property # getter prezzo
    def prezzo(self):
        return self.__prezzo

    @property # getter quantità
    def quantità(self):
        return self.__quantita

    @prezzo.setter # setter per eventuale modifica prezzo (esempio: articolo.prezzo = 99.99)
    def prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo

    @quantità.setter # setter per eventuale modifica quantità 
    def quantità(self, nuova_quantità):
        self.__quantita = nuova_quantità
        
    def descrivi(self): # restituisce descrizione completa articolo formattando prezzo con 2 decimali
        return f"Nome: {self.__nome} | Prezzo: {self.__prezzo:.2f}€ | Quantità: {self.__quantità}"