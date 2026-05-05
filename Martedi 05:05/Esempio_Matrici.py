# Matrice

matrice = [ 
    [1, 2, 3], # prima riga
    [4, 5, 6], # seconda riga
]

# for stampa uno per uno
for riga in matrice:
    for elemento in riga:
        print(elemento)


# esempio pratico - voti degli studenti per materia

studenti = [
    ["Mario", 8, 7, 9],    # nome + voti
    ["Luigi", 6, 8, 7],
    ["Sara", 9, 10, 8]
]

for studente in studenti:       # scorre ogni studente
    nome = studente[0]          # primo elemento è il nome
    voti = studente[1:]         # resto sono i voti
    print(f"\nStudente: {nome}")
    for voto in voti:           # scorre i voti dello studente
        print(f"  - Voto: {voto}")