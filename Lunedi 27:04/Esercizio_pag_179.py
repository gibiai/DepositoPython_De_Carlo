class Posto:
    def __init__(self, numero, fila):
        self.__numero = numero # numero poltrona 
        self.__fila = fila # fila poltrona
        self._occupato = False # libero di default - un underscore per permettere accesso alle sottoclassi

    def get_numero(self): # getter numero
        return self.__numero

    def get_fila(self): # getter fila
        return self.__fila

    def get_occupato(self): # getter stato occupato
        return self._occupato

    def prenota(self): # prenota se libero
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self.__numero} fila {self.__fila} prenotato!")
        else:
            print(f"Posto {self.__numero} fila {self.__fila} già occupato!")

    def libera(self): # libera se occupato
        if self._occupato:
            self._occupato = False
            print(f"Posto {self.__numero} fila {self.__fila} liberato!")
        else:
            print(f"Posto {self.__numero} fila {self.__fila} non era prenotato!")

class PostoVIP(Posto): # eredita da Posto
    def __init__(self, numero, fila, servizi_extra):
        super().__init__(numero, fila)
        self.__servizi_extra = servizi_extra # la lista di servizi extra

    def prenota(self): # override - prenota e attiva servizi extra
        super().prenota() # chiama prenota() di Posto
        print(f"Servizi extra attivati: {', '.join(self.__servizi_extra)}")

class PostoStandard(Posto): # eredita da Posto
    def __init__(self, numero, fila, costo):
        super().__init__(numero, fila)
        self.__costo = costo # costo della prenotazione

    def prenota(self): # override - prenota e mostra costo
        super().prenota() # chiama prenota() di Posto
        print(f"Costo prenotazione online: {self.__costo}€")

class Teatro:
    def __init__(self):
        self.__posti = [] # lista vuota di posti

    def aggiungi_posto(self, posto): # aggiunge posto alla lista
        self.__posti.append(posto)

    def prenota_posto(self, numero, fila): # cerca e prenota il posto
        for posto in self.__posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                return
        print(f"Posto {numero} fila {fila} non trovato!")

    def libera_posto(self, numero, fila): # cerca e libera il posto
        for posto in self.__posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.libera()
                return
        print(f"Posto {numero} fila {fila} non trovato!")

    def stampa_posti_disponibili(self): # stampa tutti i posti liberi col tipo di posto
        print("\nPosti disponibili:")
        for posto in self.__posti:
            if not posto.get_occupato():
                tipo = "VIP" if isinstance(posto, PostoVIP) else "Standard" # controlla il tipo di posto
                print(f"Posto {posto.get_numero()} fila {posto.get_fila()} ({tipo})")

    def stampa_posti_occupati(self): # stampa tutti i posti occupati
        print("\nPosti occupati:")
        for posto in self.__posti:
            if posto.get_occupato():
                print(f"Posto {posto.get_numero()} fila {posto.get_fila()}")

# Setup teatro con posti
teatro = Teatro()
teatro.aggiungi_posto(PostoVIP(1, "A", ["Accesso al lounge", "Servizio in posto"]))
teatro.aggiungi_posto(PostoVIP(2, "A", ["Accesso al lounge"]))
teatro.aggiungi_posto(PostoStandard(1, "B", 15))
teatro.aggiungi_posto(PostoStandard(2, "B", 15))
teatro.aggiungi_posto(PostoStandard(3, "B", 10))

while True:
    print("\nCosa vuoi fare?")
    print("1 - Prenota un posto")
    print("2 - Libera un posto")
    print("3 - Vedi posti occupati")
    print("4 - Esci")
    teatro.stampa_posti_disponibili() # mostra i posti liberi ad ogni ciclo
    scelta = input("Scelta: ")

    match scelta:
        case "1":
            numero = int(input("Numero posto: "))
            fila = input("Fila: ").upper() # upper() converte in caps
            teatro.prenota_posto(numero, fila)
        case "2":
            numero = int(input("Numero posto: "))
            fila = input("Fila: ").upper()
            teatro.libera_posto(numero, fila)
        case "3":
            teatro.stampa_posti_occupati()
        case "4":
            print("Arrivederci!")
            break # esce dal while
        case _:
            print("Scelta non valida!")