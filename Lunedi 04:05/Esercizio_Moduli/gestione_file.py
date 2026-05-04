# Modulo per la gestione dei file

import os # libreria per operare con file e cartelle

def salva_risultati(giorni, totale, media, sopra_media): # salva tutto su file txt
    nome_file = "risultati_vendite.txt"
    
    with open(nome_file, "a") as file: # apre e chiud in automatico, aggiungendo alla fine
        file.write("=" * 40 + "\n") # separatore viviso - cornice
        file.write("RIEPILOGO VENDITE\n")
        file.write("=" * 40 + "\n")
        
        for giorno in giorni: # cicla e dopo scrive la descrizione di ogni giorno
            file.write(giorno.descrizione() + "\n") # chiamo metodo classe Giorno - pol
            
        file.write(f"\nTotale generale: {totale:.2f}€\n") # scrive totale
        file.write(f"Media generale: {media:.2f}€\n") # scrive media
        
        if len(sopra_media) > 0: # scrive giorni se esistono 
            file.write("\nGiorni sopra la media:\n") # titolo
            for giorno in sopra_media:
                file.write(f" - {giorno.descrizione()}\n") # elenchiamo solo i giorni migliori con trattino
        else:
            file.write("\nNessun giorno sopra la media.\n") # caso contrario avvisa assenza
        
        file.write("\n") # riga vuota finale
    print(f"Risultati salvati in {nome_file}!")
    
def leggi_risultati(): # legge e stampa il file dei risultati
    try:
        with open("risultati_vendite.txt", "r") as file: # "r" legge il file
            print("\n" + file.read())
    except FileNotFoundError: # se il file non esiste
        print("Nessun risultato salvato.")
