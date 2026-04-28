from abc import ABC, abstractmethod # importo ABC per classi astratte

class VeicoloTrasporto(ABC): # classe astratta - non instanziabile direttamente
    def __init__(self, targa, peso_massimo):
        self._targa = targa # un solo _ per renderla accessibile alle sottoclassi
        self._peso_massimo = peso_massimo # capacità massima in kg protetta
        self._carico_attuale = 0 # peso parte sempre da 0

    @property # sostituisce get_targa() - legge targa senza parentesi
    def targa(self):
        return self._targa

    @property # sostituisce get_peso_massimo() - legge peso massimo senza parentesi
    def peso_massimo(self):
        return self._peso_massimo

    @property # sostituisce get_carico_attuale() - legge carico attuale senza parentesi
    def carico_attuale(self):
        return self._carico_attuale

    def carica(self, peso): # aggiunge carico se non supera il massimo / metodo concreto
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Caricati {peso}kg sul veicolo {self._targa}")
        else:
            print(f"Peso superato! Capacità rimasta: {self._peso_massimo - self._carico_attuale}kg")

    def scarica(self): # riporta il carico a 0 / metodo concreto
        self._carico_attuale = 0
        print(f"Veicolo {self._targa} scaricato!")

    @abstractmethod # decoratore che indica che ogni sottoclasse deve implementarlo / astratto
    def costo_manutenzione(self): # metodo astratto - regole diverse per ogni veicolo
        pass


class Camion(VeicoloTrasporto): # eredita da VeicoloTrasporto
    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo)
        self.__numero_assi = numero_assi # attributo specifico del camion

    def costo_manutenzione(self): # come da traccia: 100€ per asse + 1€ per kg di carico massimo
        return (100 * self.__numero_assi) + (1 * self._peso_massimo)


class Furgone(VeicoloTrasporto): # eredita da VeicoloTrasporto
    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo)
        self.__alimentazione = alimentazione # diesel o elettrico

    def costo_manutenzione(self): # come in traccia, regola: 200€ elettrico, 150€ diesel
        if self.__alimentazione == "elettrico":
            return 200
        else:
            return 150

    @property # sostituisce get_alimentazione() - legge alimentazione senza parentesi
    def alimentazione(self):
        return self.__alimentazione


class Motocarro(VeicoloTrasporto): # sempre che eredita
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.__anni_servizio = anni_servizio # anni di servizio del motocarro

    def costo_manutenzione(self): # come da traccia, regola che 50€ per anno di servizio
        return 50 * self.__anni_servizio


class GestoreFlotta:
    def __init__(self):
        self.__veicoli = [] # lista vuota dei veicoli

    def aggiungi_veicolo(self, veicolo): # aggiunge veicolo alla lista
        self.__veicoli.append(veicolo)
        print(f"Veicolo {veicolo.targa} aggiunto alla flotta!") # uso property

    def rimuovi_veicolo(self, targa): # rimuove veicolo per targa
        for veicolo in self.__veicoli:
            if veicolo.targa == targa: # uso property
                self.__veicoli.remove(veicolo)
                print(f"Veicolo {targa} rimosso dalla flotta!")
                return
        print(f"Veicolo {targa} non trovato!")

    def costo_totale_manutenzione(self): # somma costi manutenzione di tutti i veicoli
        totale = 0
        for veicolo in self.__veicoli: # polimorfismo - chiama costo_manutenzione() di ciascuno
            totale += veicolo.costo_manutenzione()
        return totale

    def carica_veicolo(self, targa, peso): # cerca veicolo per targa e lo carica
        for veicolo in self.__veicoli:
            if veicolo.targa == targa: # uso property
                veicolo.carica(peso)
                return
        print(f"Veicolo {targa} non trovato!")

    def stampa_veicoli(self): # stampa tutti i veicoli con info
        print("\n-- FLOTTA --")
        for veicolo in self.__veicoli:
            print(f"Targa: {veicolo.targa} | Tipo: {type(veicolo).__name__} | Carico: {veicolo.carico_attuale}/{veicolo.peso_massimo}kg | Manutenzione: {veicolo.costo_manutenzione()}€") # property + type().__name__ per il tipo
        print(f"Costo totale manutenzione: {self.costo_totale_manutenzione()}€")


# Setup gestore
gestore = GestoreFlotta()

# menu principale
while True: # ciclo si ripete finché vero
    print("\nCosa vuoi fare?")
    print("1 - Aggiungi veicolo")
    print("2 - Rimuovi veicolo")
    print("3 - Carica veicolo")
    print("4 - Stampa flotta")
    print("5 - Basta (stampa tutto ed esci)")

    scelta = input("Scelta: ")

    match scelta:
        case "1": # aggiunge un nuovo veicolo scelto dall'utente
            print("\nTipo veicolo:")
            print("1 - Camion")
            print("2 - Furgone")
            print("3 - Motocarro")
            tipo = input("Tipo: ")
            targa = input("Targa: ").upper()
            peso_massimo = int(input("Peso massimo (kg): "))

            match tipo: # menu annidato
                case "1":
                    numero_assi = int(input("Numero assi: "))
                    gestore.aggiungi_veicolo(Camion(targa, peso_massimo, numero_assi))
                case "2":
                    alimentazione = input("Alimentazione (diesel/elettrico): ").lower()
                    gestore.aggiungi_veicolo(Furgone(targa, peso_massimo, alimentazione))
                case "3":
                    anni_servizio = int(input("Anni di servizio: "))
                    gestore.aggiungi_veicolo(Motocarro(targa, peso_massimo, anni_servizio))
                case _:
                    print("Tipo non valido!")

        case "2": # rimuove veicolo per targa
            targa = input("Targa da rimuovere: ").upper()
            gestore.rimuovi_veicolo(targa)

        case "3": # carica un veicolo
            targa = input("Targa veicolo: ").upper()
            peso = int(input("Peso da caricare (kg): "))
            gestore.carica_veicolo(targa, peso)

        case "4": # stampa la flotta
            gestore.stampa_veicoli()

        case "5": # stampa tutto ed esce
            print("\n-- SITUAZIONE FINALE --")
            gestore.stampa_veicoli()
            print("Alla prossima!")
            break

        case _:
            print("Scelta non valida!")