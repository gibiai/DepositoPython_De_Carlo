# studente.py - Modulo gestione singolo studente loggato
class Studente: # classe per rappresentare uno studente
    def __init__(self, nome, corso):
        self._nome = nome # attributo protetto
        self._corso = corso # attributo protetto

    @property # getter legge nome senza parentesi
    def nome(self):
        return self._nome

    @property # legge corso senza parentesi
    def corso(self):
        return self._corso

    @nome.setter # modifica nome - chiamato con studente.nome = "nuovo"
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome

    @corso.setter # modifica corso - chiamato con studente.corso = "nuovo"
    def corso(self, nuovo_corso):
        self._corso = nuovo_corso

    def descrivi(self): # restituisce descrizione completa dello studente
        return f"Nome: {self._nome} | Corso: {self._corso}"
