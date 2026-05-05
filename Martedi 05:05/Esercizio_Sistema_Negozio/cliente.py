# Modulo gestione singolo cliente

class Cliente: # classe per rappresentare un cliente
    def __init__(self, nome, cognome):
        self.__nome = nome # nome privato
        self.__cognome = cognome # cognome privato
        self.__acquisti = [] # lista acquisti privata - parte vuota si riempie man man

    @property # getter nome
    def nome(self):
        return self.__nome

    @property # getter cognome
    def cognome(self):
        return self.__cognome

    @property # getter acquisti
    def acquisti(self):
        return self.__acquisti

    def aggiungi_acquisto(self, articolo, prezzo): # aggiunge acquisto alla lista
        self.__acquisti.append({"articolo": articolo, "prezzo": prezzo}) # salvo dizionario con chiavi articolo e prezzo

    def salva(self): # salva cliente e acquisti su file txt
        with open("clienti.txt", "a") as file: # apre/chiude il file e aggiunge alla fine
            for acquisto in self.__acquisti: # scorre dizionari
                file.write(f"{self.__nome},{self.__cognome},{acquisto['articolo']}:{acquisto['prezzo']}\n") # scrive riga per ogni acquisto
        print(f"Dati cliente {self.__nome} salvati!")

    def descrivi(self): # restituisce descrizione completa del cliente
        return f"Cliente: {self.__nome} {self.__cognome} | Acquisti: {len(self.__acquisti)}" # stampa tutto - len conta numeri elementi nella lista