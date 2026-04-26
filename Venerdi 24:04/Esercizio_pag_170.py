class Veicolo:
    def __init__(self, marca, modello, anno): # costruttore con attributi di istanza
        self.__marca = marca # __ attributi privati
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False # attributo interno / "spento" di default
    
    def accendi(self): # cambia status accensione su True
        self.__accensione = True
        print("Veicolo acceso")
    
    def spegni(self): # riporta status accensione su False
        self.__accensione = False
        print("Veicolo spento")
        
    def get_marca(self): # Getter Marca - legge la marca
        return self.__marca
    
    def get_modello(self): # Getter modello - legge il valore modello
        return self.__modello
    
    def get_anno(self):
        return self.__anno

class Auto(Veicolo): # Classe figlia che eredita da Veicolo
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno) # richiamo costruttore di Veicolo
        self.__numero_porte = numero_porte
        
    def suona_clacson(self): # metodo specifico di Auto
        print("Beep beep!")

class Furgone(Veicolo): # Furgone eredita da Veicolo
    def __init__(self, marca, modello, anno, capacità_carico):
        super().__init__(marca, modello, anno)
        self.__capacità_carico = capacità_carico
    
    def carica(self): # carica il furgone 
        print(f"Furgone caricato, capacità {self.__capacità_carico}kg")
    
    def scarica(self): # scarica il furgone
        print("Furgone scaricato")
        
class Motocicletta(Veicolo): # Classe figlia motocicletta che eredita da VEicolo
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno) 
        self.__tipo = tipo
        
    def esegui_wheelie(self): # metodo specifico solo se sportiva
        if self.__tipo == "sportiva":
            print("Wheelie!")
        else:
            print("Solo le moto sportive fanno wheelie!")
    
class GestoreParcoVeicoli:
    def __init__(self):
        self.__veicoli = [] # lista vuota per i veicoli da aggiungere
        
    def aggiungi_veicolo(self, veicolo): # aggiunge veicolo alla lista
        self.__veicoli.append(veicolo)
            
    def rimuovi_veicolo(self, marca, modello):
        for veicolo in self.__veicoli: # scorre tutti i veicoli
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello: # se trova quello giusto
                self.__veicoli.remove(veicolo) # lo rimuove
                break # esce dal ciclo
        
    def lista_veicoli(self): # stampa tutti i veicoli nel parco
        for veicolo in self.__veicoli:
            print(f"{veicolo.get_marca()} {veicolo.get_modello()} ({veicolo.get_anno()})")
                
# Test - creo 3 oggetti specifici
auto = Auto("Fiat", "Panda", 2020, 5)
furgone = Furgone("Mercedes", "Sprinter", 2019, 1000)
moto = Motocicletta("Ducati", "Monster", 2022, "sportiva")
# archivio questi veicoli
gestore = GestoreParcoVeicoli()
gestore.aggiungi_veicolo(auto)
gestore.aggiungi_veicolo(furgone)
gestore.aggiungi_veicolo(moto)
# "presentiamo" i veicoli salvati/presenti
gestore.lista_veicoli()
# test azioni specifiche
auto.suona_clacson()    
furgone.carica()        
moto.esegui_wheelie()
# test accensione
auto.accendi()   # accende l'auto
auto.spegni()    # spegne l'auto 