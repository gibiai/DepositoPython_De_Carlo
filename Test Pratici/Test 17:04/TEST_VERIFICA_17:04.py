""" prima fase del software : login , 5 operazioni totali
prima parte login e registrazione. registrazione come vogliamo. posizione 0 posizione 1
seconda fase due scelte nel menu, calcolatrice e stampa/mostra dati 
tutti gli addendi o tutte le operazioni 
qualsiasi miglioramento della fase di stampa aumenterà il voto del codice
e deve poter girare
non utenti con nomi uguali, tutto gestito menu inserimento dati e non si possono usare gli oggetti

(stampa dati o addendi o operazioni)
dopo 4 operazioni mi butta fuori e stampa tutti i dati (non obbligatorio)"""

# DATI - liste per tutti i valori 
# Database di tutti dati/operazioni

utenti = [] # lista dove salviamo utenti (nome e pass)
utente_loggato = [] # utente loggato al momento
operazioni = [] # lista dove salviamo operazioni eseguite
valori = [] # lista dove salviamo i valori inseriti

# FUNZIONI REGISTRA - LOGIN
# inserimento e registrazione dei dati dell'utente e successivo login

def registra():
    nome = input("Nome: ")
    for utente in utenti: # scorro gli utenti
        if utente[0] == nome: # check se nome già esistente
            print("Nome già esistente!")
    password = input("Password: ")
    utenti.append([nome, password]) # salva nome in pos iniziale (0), pass in 1
    print("Registrazione completata!")
        
def login():
    # !!! potenziale bug senza login valido?
    # utente_loggato = None 
    # uso di global utente_loggato e utente_loggato = utente
    nome = input("Nome: ")
    password = input("Password: ")
    for utente in utenti: # scorre tutti gli utenti salvati per trovare corrispondenza
        if utente[0] == nome and utente[1] == password:
            utente_loggato.append(utente) # salva utente loggato se trovato
            print("Accesso effettuato! Benvenuto", nome)
            return True # condizione soddisfatta e quindi ciclo interrotto / login riuscito
    print("Credenziali errate") # se nessun utente corrisponde
    return False
    
# FUNZIONE CALCOLATRICE
# contatore per traccia operazioni eseguite - esegue operazioni richieste
# {[(test dizionario per "storaggio" dei dati?)]}

def calcolatrice():
    contatore = 0 # conta le operazioni eseguite
    
    while contatore < 4: # lopp che dopo 4 operazioni ferma il programma
        n_input = input("Quanti numeri vuoi inserire? (o 'q' per uscire): ")
        if n_input.lower() == "q":
            print("Uscita dalla calcolatrice...")
            return
        
        n = int(n_input)
        numeri = []
        for i in range(n): # ciclo per n volte scelte utente
            num = float(input("Inserisci numero: ")) # float per accettare anche decimali
            numeri.append(num)
            valori.append(num) # storico globale
        
        scelta = input("+ = somma, - = sottrazione, * = moltiplicazione, / = divisione, % = modulo: ")
        risultato = numeri[0] # parte dal primo numero
        
        for i in range(1, len(numeri)): # applico operazione su tutti i numeri
            if scelta == "+":
                risultato += numeri[i]
            elif scelta == "-":
                risultato -= numeri[i]
            elif scelta == "*":
                risultato *= numeri[i]
            elif scelta == "/":
                if numeri[i] == 0: # controllo divisione per 0
                    print("Errore: divisione per 0!!")
                    return # fermiamo tutto e usciamo in caso di errore
                risultato /= numeri[i]
            elif scelta == "%":
                risultato %= numeri[i]
            else:
                print("Operazione non valida!")
                return # di nuovo stop per evitare errori
        
        print("Risultato:", risultato)
        operazioni.append([scelta, numeri, risultato]) # salviamo operazioni, valori e risultato
        contatore += 1
        print("Operazioni rimanenti:", 4 - contatore)
        
    print("\n--- SESSIONE TERMINATA DOPO 4 OPERAZIONI ---")
    stampa_dati() # stampa tutti i dati prima di buttar fuori
    utente_loggato.clear()

# FUNZIONE STAMPA DATI
# mostra utente connesso, tutti i valori inseriti 
# ogni tipo di operazione insieme ai numeri usati e il risultato

def stampa_dati():
    print("\n---- DATI SESSIONE ----")
    print("Utente:", utente_loggato[0][0]) # = nome utente: [0] primo utente loggato [0] nome dentro la lista utente
    print("Valori inseriti:", valori)
    print("Operazioni eseguite:")
    for op in operazioni: # scorre tutte le operazioni salvate
        print("Operazione:", op[0], "| Numeri:", op[1], "| Risultato:", op[2])

# MENU LOGIN
# visualizzazione a schermo tramite loop infinito delle scelte iniziali utente

def menu_login():
    while True:
        print("\n ---- MENU LOGIN ----")
        print("1. Registrati")
        print("2. Accedi")
        print("0. Esci")
        
        match input("Scegli: "):
            case "1":
                registra()
            case "2":
                if login():
                    menu_principale() # se il login va a buon fine entra nel menu
            case "0":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")
    
# MENU PRINCIPALE
# gestione delle operazioni da eseguire post login

def menu_principale():
    while True:
        if not utente_loggato: # ritorna al login in caso buttato fuori
            break
        print("\n---- MENU PRINCIPALE ----")
        print("1. CALCOLATRICE")
        print("2. STAMPA DATI")
        print("0. LOGOUT")
        
        match input("Scegli: "):
            case "1":
                calcolatrice()
            case "2":
                stampa_dati()
            case "0":
                utente_loggato.clear() #disconnette utente e cancella dati
                print("Logout effettuato!")
                break
            case _:
                print("Scelta non valida")
    
# AVVIO
# richiamo la funzione principale per avviare il nostro programma

menu_login()

