class Persona: # classe madre
    def __init__(self, nome, età): # definiamo costruttore
        self.__nome = nome # attributo privato
        self.__età = età # attributo privato

    def get_nome(self): # Getter nome - legge il nome 
        return self.__nome
    
    def set_nome(self, nome): # SEtter nome - modifica e salva nome se condizioni vere
        if isinstance(nome, str) and nome != "": # controlla se è una str non vuota
            self.__nome = nome # memorizziamo
    
    def get_età(self): # Getter età - legge età
        return self.__età
    
    def set_età(self, età): # Setter età - salva se condizioni True
        if isinstance(età, int) and età > 0: # check se è un int 
            self.__eta = età # sovrascrive
            
    def presentazione(self): # Stampa presentazione con nome ed età
        print(f"Mi chiamo {self.__nome} e ho {self.__età} anni")
        
class Studente(Persona): # Classe figlia eredita da Persona
    def __init__(self, nome, età, voti): # voti: attributo di istanza specifico per ogni Studente
        super().__init__(nome, età) # chiama il costruttore di Persona per non riscrivere nome/età
        self.voti = voti
    
    def calcola_media(self): # Restituisce la media dei voti
        return sum(self.voti) / len(self.voti)
    
    def presentazione(self): # Override - aggiunge la media alla presentazione
        print(f"Mi chiamo {self.get_nome()}, ho {self.get_età()} anni e la mia media è {self.calcola_media()}")

class Professore(Persona): # Classe figlia di Persona sempre
    def __init__(self, nome, età, materia): 
        super().__init__(nome, età) # richiama sempre il costruttore di Persona
        self.materia = materia
    
    def presentazione(self): # Altro override - aggiunge materia alla presentazione
        print(f"Mi chiamo {self.get_nome()}, ho {self.get_età()} anni e insegno {self.materia}")
        
# Test
studente = Studente("Mario", 20, [8, 7, 9, 6])  # crea uno studente con nome, età e lista voti
professore = Professore("Prof. Rossi", 45, "Matematica")  # crea un professore con nome, età e materia

# chiamata del metodo presentazione che agisce in base al comportamento diverso in base all'oggetto
studente.presentazione()    # chiama presentazione() di Studente 
professore.presentazione()  # chiama presentazione() di Professore