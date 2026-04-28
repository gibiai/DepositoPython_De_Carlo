from abc import ABC, abstractmethod # importo libreria ABC per classi astratte (esisto solo per sottoclassi)

class Impiegato(ABC): # ABC rende la classe astratta
    def __init__(self, nome, cognome, stipendio_base): # costruttore che inizializza attributi con parametri forniti
        self.__nome = nome # attributi che saranno comuni per tutte le sottoclassi
        self.__cognome = cognome # cognome impiegato privato
        self.__stipendio_base = stipendio_base # stipendio base privato
        
    def get_nome(self): # getter nome
        return self.__nome
    
    def get_cognome(self): # getter cognome
        return self.__cognome
    
    def get_stipendio_base(self): # getter stipendio base
        return self.__stipendio_base
    
    @abstractmethod # decoratore - forza le sottoclassi ad implementare questo metodo (restituisce errore se non presente)
    def calcola_stipendio(self): # metodo abstratto, vuoto, da implementare
        pass
    
    
class ImpiegatoFisso(Impiegato): # eredita da Impiegato
    def calcola_stipendio(self): # implementazione - stipendio fisso senza modifiche
        return self.get_stipendio_base()
    
class ImpiegatoAProvvigione(Impiegato): # eredita da impiegato
    def __init__(self, nome, cognome, stipendio_base, vendite, percentuale):
        super().__init__(nome, cognome, stipendio_base)
        self.__vendite = vendite # totale vendite effettuate
        self.__percentuale = percentuale # percentuale bonus sulle vendite
        
    def calcola_stipendio(self): # implementazione - stipendio base + bonus vendite
        bonus = self.__vendite * self.__percentuale # calcola il bonus
        return self.get_stipendio_base() + bonus # restituisce stipendio + bonus
    
def stampa_impiegato(impiegato): # funzione che stampa info e stipendio
    print(f"{impiegato.get_nome()} {impiegato.get_cognome()} - Stipendio: {impiegato.calcola_stipendio()}€")
    

# Test
fisso = ImpiegatoFisso("Mario", "Rossi", 2000)
provvigione = ImpiegatoAProvvigione("Giuseppe", "Bianchi", 1500, 10000, 0.05) # 5% su 10.000 di vendite

stampa_impiegato(fisso)
stampa_impiegato(provvigione)