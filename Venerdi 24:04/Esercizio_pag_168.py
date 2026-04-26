class ContoBancario:
    def __init__(self, titolare, saldo): # definiamo costruttore e attributi di istanza
        self.__titolare = titolare # attributo privato
        self.__saldo = saldo # attributo privato
    
    def deposita(self, importo): # Metodo deposito (aggiunge se saldo positivo)
        if importo > 0:
            self.__saldo += importo
            print(f"Depositati {importo}€")
        else:
            print("Importo non valido!")
    
    def preleva(self, importo): # Metodo prelievo (sottrae se ci sono fondi)
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelevati {importo}€")
        else:
            print("Operazione non valida")
    
    def visualizza_saldo(self): # Restituisce saldo corrente senza modifiche
        return self.__saldo
    
    def get_titolare(self): # Getter Titolare - legge nome del titolare
        return self.__titolare
            
    def set_titolare(self, titolare): # Setter Titolare - modifica e salva solo se condizioni vere
        if isinstance(titolare, str) and titolare != "": # controllo se la istanza è di tipo str
            self.__titolare = titolare # se condizioni vere sovrascrive

# Test - chiamata ai metodi di istanza
conto = ContoBancario("Mario Rossi", 1000)
print(conto.get_titolare())     
print(conto.visualizza_saldo()) 
conto.deposita(500)
print(conto.visualizza_saldo()) 
conto.preleva(200)
print(conto.visualizza_saldo()) 