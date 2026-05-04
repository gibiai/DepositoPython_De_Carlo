# utente.py - Modulo gestione utente
from abc import ABC, abstractmethod # importo ABC per classi astratte

class Utente(ABC): # classe astratta - non instanziabile direttamente
    def __init__(self, nome, password):
        self._nome = nome # attributo protetto - accessibile alle sottoclassi
        self._password = password # attributo protetto - accessibile alle sottoclassi

    @property # sostituisce getter legge nome senza parentesi
    def nome(self):
        return self._nome

    @abstractmethod # obbliga le sottoclassi ad implementarlo
    def menu(self): # metodo astratto - comportamento diverso per ogni sottoclasse
        pass

class StudenteUtente(Utente): # classe utente normale - eredita da Utente
    def menu(self): # implementazione metodo astratto - comportamento specifico utente
        return "Menu studente"

class Admin(Utente): # classe admin - eredita da Utente
    def __init__(self):
        super().__init__("admin", "admin") # credenziali hardcodate - non si registra

    def menu(self): # override - comportamento specifico admin
        return "Menu admin"

    def reset(self, motivazione): # metodo esclusivo admin - salva log motivazione
        print(f"Reset eseguito da {self.nome} - Motivo: {motivazione}")
