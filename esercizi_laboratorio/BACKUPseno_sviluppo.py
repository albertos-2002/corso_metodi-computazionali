import os
# Set the QT_QPA_PLATFORM environment variable
os.environ['QT_QPA_PLATFORM'] = 'xcb'

#-----------------------------------------------------------------

from matplotlib import pyplot as plt
import numpy as np
import math

"""
Esercizio:
Grafico della funzione seno e del suo polinomio di taylor

note prof:
- fare la funzione per il factorial

note:
- per svilluppo cuttare y > 5
"""

# variabili globali ----------------------------------------------------------

#essendo l'intervallo simmetrico il risultato migliore si ha per x<25
#x=10 da un buon risultato
xMax = 4
NumeroPunti = 50000
OrdinePolinomio = 2

ascissePositive = []
ascisseNegative = []
ascisse = []
sinFunction = []
taylorPol = []

# simmettrizzazione dell'intervallo (versione laboriosa) --------------------
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

#calcolo della funzione seno -----------------------------------------------

for element in ascisse:
    sinFunction.append( np.sin(element) )

#polinomio di taylor ------------------------------------------------------
"""
Ricordiamo la formula della serie di taylor (maclaurin) per il seno
serie n=0 to n=inf of (-1)^n / (2n+1)! x^(2n+1)
"""

for element in ascisse:
    dummy = 0
    for n in range(OrdinePolinomio+1): #arriviamo così fino ad ordine n e non n-1
        dummyExp = 2*n +1
        dummy += (-1)**n / math.factorial( dummyExp ) * element**dummyExp
    taylorPol.append(dummy)

#creazione del grafico ("metodo colab notebook") ---------------------------

plt.plot( ascisse, sinFunction, linestyle="--", color="orange", label="Sen Function" )
plt.plot( ascisse, taylorPol, linestyle=(0, (1, 5)), color="green", label="Taylor seriess" )

#disegno degli assi
plt.axhline( 0, color='grey', linestyle=(0, (1, 3)) )  # Horizontal axis
plt.axvline( 0, color='grey', linestyle=(0, (1, 3)) )  # Vertical axis

#abbellimento grafico
plt.title( "Seno e polinomio di taylor" )
plt.xlabel( "Angolo" )
plt.ylabel( "Seno" )
plt.legend()
plt.grid()
plt.show()
