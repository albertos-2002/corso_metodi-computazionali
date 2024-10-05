import os
# Set the QT_QPA_PLATFORM environment variable
os.environ['QT_QPA_PLATFORM'] = 'xcb'

#import matplotlib
#matplotlib.use('QtAgg')
#check the backend
#print("Current backend:", matplotlib.get_backend()) 

#-----------------------------------------------------------------

from matplotlib import pyplot as plt
import numpy as np



"""
Esercizio:
Grafico della funzione seno e del suo polinomio di taylor
"""

#variabili globali
xMax = 50
NumeroPunti = 5000
OrdinePolinomio = 5


# simmettrizzazione dell'intervallo (versione laboriosa)

ascissePositive = []
ascisseNegative = []
ascisse = []
sinFunction = []

for index in range( NumeroPunti ): #crea indici da 0 a n-1
    ascissePositive.append( xMax/NumeroPunti*index )

"""
utilizzando la funzione range in modo "più" complesso

le liste hanno indice che va da 0 a n-1
il primo termine si riferisce al valore max
il secondo termine è quello di stop NON INCLUSO
il terzo termine è quello di step

in questo modo creiamo un range che parte da n-1, decresci di una 
unità ad ogni interazione e si ferma a 0, comprendo in questo modo 
tutti gli elementi della lista in ordine inverso
"""

for index in range( NumeroPunti -1, -1, -1 ):
    ascisseNegative.append( -ascissePositive[index] )

ascisse = ascisseNegative + ascissePositive

#calcolo della funzione seno

for element in ascisse:
    sinFunction.append( np.sin(element) )

#creazione del grafico ("metodo colab notebook")

plt.plot( ascisse, sinFunction, linestyle="--", color="orange", label="Sen Function" )
plt.title("Seno e polinomio di taylor")
plt.xlabel("Angolo")
plt.ylabel("Seno")
plt.legend()
plt.grid()
plt.show()
