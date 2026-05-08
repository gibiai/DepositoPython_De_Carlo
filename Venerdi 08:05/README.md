🍽️ Ristorante — Gestionale Intelligente
---

👤 Progetto Individuale
Progetto sviluppato per applicare i principi della Programmazione Orientata agli Oggetti in un contesto realistico di gestione ristorativa.
Autore: Gabriele De Carlo

---

🎯 Obiettivi del Progetto

Modellare una gerarchia di piatti: Antipasto, Primo, Secondo
Applicare i principi fondamentali della Programmazione Orientata agli Oggetti
Gestire un catalogo di piatti tramite operazioni CRUD (crea, modifica, elimina)
Leggere e scrivere dati su file CSV e TXT
Analizzare i dati del menu tramite filter() e statistiche base
Visualizzare i dati tramite grafici con matplotlib (appendice)

---

🛠️ Tech Stack

Python 3.10+
OOP (Encapsulation, Inheritance, Polymorphism, Abstraction)
ABC e @abstractmethod per le classi astratte
@property e setter con validazione per l'incapsulamento
filter() per l'analisi dei dati
Modulo csv per la lettura e scrittura del catalogo
File .txt per ordini e recensioni
matplotlib per la visualizzazione grafica

---

📂 Project Structure

models.py — Classe astratta Piatto e sottoclassi Antipasto, Primo, Secondo
gestionale.py — Classe Gestionale: unico oggetto polimorfico centrale
file_manager.py — Lettura e scrittura di menu.csv, ordini.txt, recensioni.txt
analisi.py — Analisi statistiche e filtri sui dati del menu
visualizza.py — Grafici con matplotlib (appendice)
main.py — Entry point e menu principale

---

⚙️ Setup

Installare matplotlib: pip install matplotlib
Eseguire con python3 main.py
Nessun file necessario: menu.csv, ordini.txt e recensioni.txt vengono creati automaticamente al primo utilizzo

---

🧱 Core Classes

Piatto — classe astratta con @abstractmethod su descrivi() e get_tipo(), __prezzo privato con @property e setter con validazione
Antipasto — sottoclasse con attributo specifico porzione
Primo — sottoclasse con attributo specifico tipo_pasta
Secondo — sottoclasse con attributo specifico cottura
Gestionale — classe centrale con aggiungi(), cerca(), modifica(), elimina(), visualizza_tutti(), crea_piatto()

---

📊 Functional Workflow

Avvio del programma e caricamento automatico da menu.csv (se esiste)
Inserimento manuale di piatti tramite menu CRUD
Modifica o eliminazione di piatti esistenti tramite codice
Salvataggio del catalogo su menu.csv
Registrazione ordini e recensioni su file TXT
Analisi del menu (statistiche, filtro per tipo, filtro per prezzo)
Visualizzazione grafica tramite sottomenu dedicato (appendice)

---

📈 Key Learning Outcomes

Incapsulamento — __prezzo privato accessibile solo tramite @property e setter con validazione
Ereditarietà — le sottoclassi ereditano da Piatto tramite super()
Polimorfismo — .descrivi() e .get_tipo() overridati in ogni sottoclasse
Astrazione — Piatto è classe astratta (ABC) non istanziabile direttamente
Filter — filter() con lambda per filtrare piatti per tipo e fascia di prezzo
I/O — lettura e scrittura con with open, modalità r, w, a, encoding UTF-8
Modularità — ogni file ha una responsabilità specifica

---

📊 Esempi di Output


---

📄 License
This project is intended for educational purposes and practical OOP training. 
