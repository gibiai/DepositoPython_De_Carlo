# CLASSE MADRE
class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

# CLASSE FIGLIA - Elettronica
class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia # attributo specifico questa classe

    def mostra_info(self):
        print(f"Prodotto: {self.nome}")
        print(f"Prezzo vendita: {self.prezzo_vendita}€")
        print(f"Garanzia: {self.garanzia} anni")
        print(f"Profitto: {self.calcola_profitto()}€")
        
# CLASSE FIGLIA - Abbigliamento
class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
    def mostra_info(self):
        print(f"Prodotto: {self.nome}")
        print(f"Prezzo vendita: {self.prezzo_vendita}€")
        print(f"Materiale: {self.materiale}")
        print(f"Profitto: {self.calcola_profitto()}€")
        
# CLASSE FABBRICA
class Fabbrica:
    def __init__(self): # inizializzo inventario come lista vuota
        self.inventario = []  # lista: [prodotto, quantità]

    def aggiungi_prodotto(self, prodotto, quantita):
        for voce in self.inventario: # controllo se già esistente
            if voce[0].nome == prodotto.nome:
                voce[1] += quantita
                print(f"Aggiunte {quantita} unità a {prodotto.nome}")
                return
        self.inventario.append([prodotto, quantita])  # caso contrario, lo aggiunge alla lista
        print(f"{quantita} unità di {prodotto.nome} aggiunte all'inventario")

    def vendi_prodotto(self, nome, quantita): # modulo per diminuire quantità e calcolare profitto
        for voce in self.inventario:
            if voce[0].nome == nome:
                if voce[1] < quantita: # check se quantità minore della richiesta
                    print("Quantità insufficiente") 
                    return
                voce[1] -= quantita # se sufficiente sottraggo
                profitto = voce[0].calcola_profitto() * quantita # uso metodo classe prodotto
                                                                 # e lo moltiplico per numero pezzi venduti

                print(f"Vendute {quantita} unità di {nome}")
                print(f"Profitto totale: {profitto}€")
                return

        print(f"{nome} non trovato")

    def resi_prodotto(self, nome, quantita): # gestisco eventuali resi, aumentando di nuovo la quantità
        for voce in self.inventario:
            if voce[0].nome == nome:
                voce[1] += quantita
                print(f"{quantita} unità di {nome} restituite")
                return

        print(f"{nome} non trovato")
        
# TEST
e = Elettronica("iPhone", 500, 999, 2)
a = Abbigliamento("Jeans", 20, 89, "Denim")

e.mostra_info()
a.mostra_info()

f = Fabbrica()
f.aggiungi_prodotto(e)
f.aggiungi_prodotto(a)

f.vendi_prodotto("iPhone")
f.resi_prodotto(e)
f.vendi_prodotto("Tastiera")  # prodotto non esistente