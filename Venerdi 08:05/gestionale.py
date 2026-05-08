# modulo che definisce la classe Gestionale
# è l'unico oggetto centrale del programma: contiene la lista piatti
# e coordina tutte le operazioni CRUD in modo polimorfico
from models import Antipasto, Primo, Secondo


# classe Gestionale: unico oggetto polimorfico che gestisce tutti i piatti
# il main crea una sola istanza di questa classe e la passa a tutti i moduli
class Gestionale:

    def __init__(self): # inizializza la lista vuota che conterrà tutti i piatti
        # lista unica per tutti i tipi di piatto 
        self.piatti = []

    def aggiungi(self, piatto): # metodo che aggiunge un piatto alla lista
        self.piatti.append(piatto)
        print(f"\nPiatto '{piatto.nome}' aggiunto!")

    # metodo che cerca un piatto tramite codice e lo restituisce
    # restituisce None se non lo trova invece di crashare
    def cerca(self, codice):
        for piatto in self.piatti:
            if piatto.codice == codice:
                return piatto
        return None

    # metodo polimorfico: stampa tutti i piatti chiamando .descrivi() su ognuno
    # Python decide da solo quale versione chiamare in base al tipo reale dell'oggetto
    def visualizza_tutti(self):
        if not self.piatti:
            print("Nessun piatto nel menu.")
            return
        print("\n--- MENU RISTORANTE ---")
        for piatto in self.piatti:
            piatto.descrivi()  # polimorfico: Antipasto, Primo o Secondo

    # metodo che modifica gli attributi di un piatto trovato tramite codice
    def modifica(self, codice):
        piatto = self.cerca(codice)
        if not piatto:
            print("Codice non trovato.")
            return

        piatto.descrivi()
        print("\nCosa vuoi modificare?")
        print("1. Nome")
        print("2. Prezzo")
        print("3. Categoria")
        scelta = input("Scelta: ").strip()

        match scelta:
            case "1":
                piatto.nome = input("Nuovo nome: ").strip()
                print("Nome aggiornato!")
            case "2":
                # usa il setter della property: valida automaticamente il valore
                piatto.prezzo = float(input("Nuovo prezzo (€): "))
                print("Prezzo aggiornato!")
            case "3":
                piatto.categoria = input("Nuova categoria: ").strip()
                print("Categoria aggiornata!")
            case _:
                print("Scelta non valida.")

    # metodo che rimuove un piatto dalla lista dopo conferma utente
    def elimina(self, codice):
        piatto = self.cerca(codice)
        if not piatto:
            print("Codice non trovato!")
            return

        piatto.descrivi()
        conferma = input("\nConfermi l'eliminazione? (s/n): ").strip().lower() # preveniamo spazi e scritte maiuscole
        if conferma == "s":
            self.piatti.remove(piatto)
            print("Eliminato!")
        else:
            print("Eliminazione annullata.")

    # metodo che chiede i dati all'utente e crea il tipo di piatto scelto
    # serie di strip per datacleaning (evitiamo spazi o errori invisibili)
    def crea_piatto(self):
        print("\n--- Aggiungi piatto ---")
        print("1. Antipasto")
        print("2. Primo")
        print("3. Secondo")
        scelta = input("Tipo: ").strip()

        # attributi comuni a tutti i piatti
        codice    = input("Codice: ").strip()
        nome      = input("Nome: ").strip()
        categoria = input("Categoria: ").strip()
        # float() converte la stringa in numero decimale
        prezzo    = float(input("Prezzo (€): "))

        # in base alla scelta chiede l'attributo specifico e istanzia la classe corrispondente
        match scelta:
            case "1":
                porzione = input("Porzione (individuale/da condividere): ").strip()
                piatto = Antipasto(codice, nome, categoria, prezzo, porzione)
            case "2":
                tipo_pasta = input("Tipo pasta (fresca/secca): ").strip()
                piatto = Primo(codice, nome, categoria, prezzo, tipo_pasta)
            case "3":
                cottura = input("Cottura (alla griglia/al forno/...): ").strip()
                piatto = Secondo(codice, nome, categoria, prezzo, cottura)
            case _:
                print("Scelta non valida.")
                return

       # Invoca il metodo interno della classe per aggiornare la lista dei dati aggiungendo l'oggetto piatto.
        self.aggiungi(piatto)