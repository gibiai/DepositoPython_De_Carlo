import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# posso impostare parametri all'inizio così setta per tutti 
plt.rcParams['figure.figsize'] = [10, 6]
plt.rcParams['figure.dpi'] = 100
plt.rcParams['figure.facecolor'] = 'green' # imposta il colore per tutti

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure # imposta il grafico - se metto per ogni grafico apre poi insieme facendo show alla fine
plt.plot(x, y) # costruisce il grafico con informazioni che vogliamo: x, y

plt.title("Grafico a linee") # titolo del grafico
plt.xlabel("X") # etichetta assi
plt.ylabel("Y") # etichecca assi

# plt.show() # apro la finestra per mostrare il grafico

# cambiando plot cambio il tipo di grafico

categorie = ['A', 'B', 'C', 'D', 'E']
valori = [3, 7, 2, 5, 8]
plt.figure()
plt.bar(categorie, valori) # grafico a barre
plt.title("Grafico a barre")
plt.xlabel("Categorie")
plt.ylabel("Valori")


# HIST
plt.figure()
data = np.random.rand(1000)
plt.hist(data, bins=30)
plt.title("Istogramma")
plt.xlabel("Valori")
plt.ylabel("Frequenza")

# Scatterplot
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title("Scatterplot")
plt.xlabel("X")
plt.ylabel("Y")

# stampo tutti 
# plt.show()

# Subplot
fig, axes = plt.subplots(nrows= 2, ncols=2, figsize=(10, 8))
axes[0, 0].plot([1,2,3,4], [1,4,6,9])
axes[0, 0].set_title('Grafico 1: Line')

axes[0, 1].scatter([1, 2, 3, 4], [2, 3, 2, 4])
axes[0, 1].set_title("Grafico 2: Scatter")

axes[1, 1].bar(categorie, valori)
axes[1, 1].set_title("Grafico 3: Barra")

plt.show()

# Seaborn - si appoggia su matplot ed è integrato con database di Pandas, maggiore ottimizzazione
# e maggiore stilizzazione

sns.set_theme(style='darkgrid') # setto il tema in anticipo

# grafico a linee
plt.figure()
tips = sns.load_dataset("tips")
print(tips.head())
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Conto totale del giorno")

# grafico linescat
plt.figure()
fmri = sns.load_dataset("fmri")
print(fmri.head())
sns.lineplot(x="timepoint", y="signal", data=fmri)
plt.title("Segnale fmri nel tempo")

plt.show()