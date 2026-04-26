# Metoto str
class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        
    def __str__(self):
        return f"{self.titolo} scritto da {self.autore}"
    
l1 = Libro("Il Signore degli Anelli", "Tolkien")
print(l1)

# Metodo len
class Squadra:
    def __init__(self, giocatori):
        self.giocatori = giocatori
    
    def __len__(self):
        return len(self.giocatori)
team = Squadra(["Marco","Luca","Anna"])
print(len(team))

team1 = ["Marco", "Luca", "Anna"]
print(len(team1))