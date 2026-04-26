## --- CLASSE BASE ---

class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} si sta spostando sul campo di battaglia.")

    def attacca(self):
        print(f"L'unità {self.nome} sta aprendo il fuoco contro il nemico!")

    def ritira(self):
        print(f"L'unità {self.nome} sta effettuando un ritiro strategico ordinato.")

    # Metodo speciale per stampare l'oggetto in modo leggibile
    def __str__(self):
        return f"[Unità: {self.nome} | Soldati: {self.numero_soldati}]"


## --- CLASSI DERIVATE (SPECIALIZZATE) ---

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome}: Trincee completate. Difesa aumentata.")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome}: Pezzi calibrati. Pronti per il bombardamento.")

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome}: Terreno esplorato. Posizioni nemiche individuate.")

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome}: Rifornimenti consegnati con successo.")

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome}: Missione di sorveglianza in corso. Nessun rumore.")


## --- CLASSE DI CONTROLLO (EREDITARIETÀ MULTIPLA) ---

# Questa classe eredita da TUTTE le classi precedenti
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        # Inizializziamo il dizionario per registrare le unità
        self.unita_registrate = {}

    def registra_unita(self, unita):
        # Aggiungiamo l'oggetto unita al dizionario usando il nome come chiave
        self.unita_registrate[unita.nome] = unita
        print(f"Sistema: {unita.nome} è stata registrata nel comando centrale.")

    def mostra_unita(self):
        print("\n--- ELENCO UNITÀ SUL CAMPO ---")
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
        else:
            for nome in self.unita_registrate:
                print(f"- {nome}")

    def dettagli_unita(self, nome):
        print(f"\n--- DETTAGLI PER {nome.upper()} ---")
        unita = self.unita_registrate.get(nome)
        if unita:
            # Usiamo il metodo speciale __str__ definito nell'UnitaMilitare
            print(unita)
        else:
            print("Errore: Unità non trovata nel registro.")


## --- TEST PROGRAMMA ---

# 1. Creiamo il centro di comando
comando = ControlloMilitare()

# 2. Creiamo alcune unità specifiche
fante1 = Fanteria("Legione X", 150)
cannone1 = Artiglieria("Tuono Selvaggio", 40)
esploratore1 = Ricognizione("Ombra Nero", 10)

# 3. Registriamo le unità
comando.registra_unita(fante1)
comando.registra_unita(cannone1)
comando.registra_unita(esploratore1)

# 4. Usiamo i metodi speciali delle unità
fante1.costruisci_trincea()
cannone1.calibra_artiglieria()

# 5. Gestione comando
comando.mostra_unita()
comando.dettagli_unita("Legione X")