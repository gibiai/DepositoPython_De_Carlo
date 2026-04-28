from abc import ABC, abstractmethod # importo libreria ABC per classi astratte

class VeicoloTrasporto(ABC): # classe astratta - non instanziabile direttamente
    def __init__(self, targa, peso_massimo):
        self._targa = targa # un solo _ per renderla accessibile alle sottoclassi
        self._peso_massimo = peso_massimo # capacità massima in kg protetta
        self._carico_attuale = 0 # peso parte sempre da 0

    def get_targa(self): # getter targa
        return self._targa

    def get_peso_massimo(self): # getter peso massimo
        return self._peso_massimo

    def get_carico_attuale(self): # getter carico attuale
        return self._carico_attuale

    def carica(self, peso): # controlla se non supera il massimo in caso aggiunge / metodo concreto
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


class Camion(VeicoloTrasporto): # classe figlia, eredita da VeicoloTrasporto
    def __init__(self, targa, peso_massimo, numero_assi): # costruttore (aggiungo numero assi)
        super().__init__(targa, peso_massimo) # chiamo costruttore classe madre
        self.__numero_assi = numero_assi # attributo specifico del camion

    def costo_manutenzione(self): # come da traccia: 100€ per asse + 1€ per kg di carico massimo
        return (100 * self.__numero_assi) + (1 * self._peso_massimo)


class Furgone(VeicoloTrasporto): # eredita da VeicoloTrasporto
    def __init__(self, targa, peso_massimo, alimentazione): # costruttore (aggiungo alimentazione)
        super().__init__(targa, peso_massimo) # chiamo costruttore classe madre
        self.__alimentazione = alimentazione # diesel o elettrico

    def costo_manutenzione(self): # come in traccia, regola: 200€ elettrico, 150€ diesel
        if self.__alimentazione == "elettrico":
            return 200
        else:
            return 150

    def get_alimentazione(self): # getter alimentazione
        return self.__alimentazione


class Motocarro(VeicoloTrasporto): # sempre che eredita
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.__anni_servizio = anni_servizio # anni di servizio del motocarro

    def costo_manutenzione(self): # come da traccia, regola che 50€ per anno di servizio
        return 50 * self.__anni_servizio


class GestoreFlotta: # classe che gestisce i veicoli
    def __init__(self):
        self.__veicoli = [] # lista vuota dei veicoli

    def aggiungi_veicolo(self, veicolo): # aggiunge un oggetto qualsiasi veicolo alla lista
        self.__veicoli.append(veicolo)
        print(f"Veicolo {veicolo.get_targa()} aggiunto alla flotta!")

    def rimuovi_veicolo(self, targa): # rimuove veicolo per targa
        for veicolo in self.__veicoli: # scorre lista e rimuove per targa
            if veicolo.get_targa() == targa:
                self.__veicoli.remove(veicolo)
                print(f"Veicolo {targa} rimosso dalla flotta!")
                return
        print(f"Veicolo {targa} non trovato!")

    def costo_totale_manutenzione(self): # polimorfismo - chiama costo_manutenzione() di ciascuno
        totale = 0
        for veicolo in self.__veicoli: # somma costi manutenzione di tutti i veicoli
            totale += veicolo.costo_manutenzione()
        return totale

    def carica_veicolo(self, targa, peso): # scorre lista per cercare veicolo per targa e lo carica
        for veicolo in self.__veicoli:
            if veicolo.get_targa() == targa:
                veicolo.carica(peso)
                return
        print(f"Veicolo {targa} non trovato!")

    def stampa_veicoli(self): # scorre veicoli nella lista e stampa tutti i veicoli con info
        print("\n-- FLOTTA --")
        for veicolo in self.__veicoli:
            print(f"Targa: {veicolo.get_targa()} | Tipo: {type(veicolo).__name__} | Carico: {veicolo.get_carico_attuale()}/{veicolo.get_peso_massimo()}kg | Manutenzione: {veicolo.costo_manutenzione()}€") # type().__name__ restituisce il nome della classe automaticamente
        print(f"Costo totale manutenzione: {self.costo_totale_manutenzione()}€") # stampa costo totale sommato


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
        case "1": # aggiunge un nuovo veicolo scelto dall'utente con menu annidato
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