import math # importo libreria per la radice quadrata

# ESERCIZIO 1 - Classe Punto
class Punto: # creo classe
    def __init__(self, x, y): # costruttore: crea il punto
        self.x = x # salva valore in oggetto x
        self.y = y # salva valore in oggetto y
        
    def muovi(self, dx, dy): # metodo per spostare il punto
        self.x += dx # aggiorna x sommando dx
        self.y += dy # aggiorna y sommando dy
        
    def distanza_da_origine(self): 
        return math.sqrt(self.x ** 2 + self.y ** 2) # formula matematica radice quadrata per calcolare 
                                                    # quanto il punto è lontano dallo (0, 0) 
    
x = float(input("Inserisci x: ")) # prende x dall'utente
y = float(input("Inserisci y: ")) # prende y dall'utente
p = Punto(x, y) # crea oggetto Punto
dx = float(input("quanto vuoi spostare x (dx)? ")) # input spostamento x
dy = float(input("Quanto vuoi spostare y (dy)? ")) # input spostamento y

p.muovi(dx, dy) # chiama metodo per spostare Punto

print("Nuova posizione:", p.x, p.y)
print("Distanza dall'origine:", p.distanza_da_origine())


# ESERCIZIO 2 - Classe Libro
class Libro:
    def __init__(self, titolo, autore, pagine): # costruttore del Libro
        self.titolo = titolo # salva valore in titolo
        self.autore = autore # salva valore in autore
        self.pagine = pagine # salva valore in pagine 
    
    def descrizione(self): # metodo che crea una frase descrittiva
        return f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine."
    
'''
# Alternativa con input da utente per Libro
titolo = input("Inserisci il titolo del libro: ")   # input titolo
autore = input("Inserisci l'autore: ")              # input autore
pagine = int(input("Inserisci numero di pagine: ")) # input pagine (numero)
libro = Libro(titolo, autore, pagine)  # crea oggetto Libro
print(libro.descrizione())
'''

libro = Libro("Fluent Python", "Luciano Ramalho", 1012) # crea oggetto Libro
print(libro.descrizione()) # stampa descrizione del libro