# Dizionari
studente = {
        "nome": "Alice",
        "età": 20,
        "sesso": "Femmina"
}

# esempio per accedere
studente = {
        "nome": "Alice",
        "età": 20,
        "sesso": "Femmina"
}

print(studente["nome"]) # Output: "Alice"
print(studente["età"]) # Output: 20

# esempio modifica
studente = {
        "nome": "Alice",
        "età": 20,
        "sesso": "Femmina"
}

studente["età"] = 21
print(studente)

# Output: {'nome: 'Alice', 'età': 21, 'sesso': 'Femmina'}

# esempio aggiunta (infinite chiavi)
studente = {
        "nome": "Alice",
        "età": 20,
        "sesso": "Femmina"
}

studente["citta"] = "Roma"
print(studente)

# Output: {'nome': 'Alice', 'età': 21, 'sesso':'Femmina', 'città': 'Roma'}
