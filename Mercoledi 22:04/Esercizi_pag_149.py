# CLASSE BASE
class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        print(f"Nome: {self.nome}, Età: {self.eta}")


# CLASSE FIGLIA - Giocatore
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        MembroSquadra.__init__(self, nome, eta)  # chiama il costruttore della classe madre
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        MembroSquadra.descrivi(self)  # stampa prima le info della classe madre
        print(f"Ruolo: {self.ruolo}, Maglia: {self.numero_maglia}")

    def gioca_partita(self):
        print(f"{self.nome} gioca come {self.ruolo}")


# CLASSE FIGLIA - Allenatore
class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        MembroSquadra.__init__(self, nome, eta)  # chiama il costruttore della classe madre
        self.anni_di_esperienza = anni_di_esperienza

    def descrivi(self):
        MembroSquadra.descrivi(self)  # stampa prima le info della classe madre
        print(f"Anni di esperienza: {self.anni_di_esperienza}")

    def dirige_allenamento(self):
        print(f"{self.nome} dirige l'allenamento con {self.anni_di_esperienza} anni di esperienza")


# CLASSE FIGLIA - Assistente
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        MembroSquadra.__init__(self, nome, eta)  # chiama il costruttore della classe madre
        self.specializzazione = specializzazione

    def descrivi(self):
        MembroSquadra.descrivi(self)  # stampa prima le info della classe madre
        print(f"Specializzazione: {self.specializzazione}")

    def supporta_team(self):
        print(f"{self.nome} supporta il team come {self.specializzazione}")


# CLASSE SQUADRA - gestisce tutti i membri e le partite
class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.membri = []  # lista che contiene tutti i membri della squadra

    def aggiungi_membro(self, membro):
        self.membri.append(membro)  # aggiunge qualsiasi tipo di membro alla lista
        print(f"{membro.nome} aggiunto alla squadra {self.nome}")

    def descrivi_squadra(self):
        print(f"\n=== Squadra {self.nome} ===")
        for membro in self.membri:
            membro.descrivi()  # chiama descrivi() su ogni membro — polimorfismo (ognuno eseguirà diversamente)
            print("---")

    def gioca_contro(self, altra_squadra):
        print(f"\n{self.nome} VS {altra_squadra.nome}")
        for membro in self.membri:
            if isinstance(membro, Giocatore):  # solo i giocatori partecipano alla partita
                membro.gioca_partita()
        for membro in altra_squadra.membri:
            if isinstance(membro, Giocatore):  # stessa cosa per l'altra squadra
                membro.gioca_partita()
        print(f"Partita terminata!")


# TEST - Squadra 1
s1 = Squadra("Inter")
s1.aggiungi_membro(Giocatore("Lautaro", 26, "Attaccante", 10))
s1.aggiungi_membro(Giocatore("Bastoni", 25, "Difensore", 95))
s1.aggiungi_membro(Allenatore("Inzaghi", 48, 10))
s1.aggiungi_membro(Assistente("Farris", 45, "Fisioterapista"))

# TEST - Squadra 2
s2 = Squadra("Milan")
s2.aggiungi_membro(Giocatore("Leao", 25, "Attaccante", 10))
s2.aggiungi_membro(Giocatore("Tomori", 26, "Difensore", 23))
s2.aggiungi_membro(Allenatore("Pioli", 58, 20))
s2.aggiungi_membro(Assistente("Bonera", 42, "Analista di gioco"))

# DESCRIZIONE SQUADRE
s1.descrivi_squadra()
s2.descrivi_squadra()

# PARTITA
s1.gioca_contro(s2)