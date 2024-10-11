import os
import sys
# Set the QT_QPA_PLATFORM environment variable
os.environ['QT_QPA_PLATFORM'] = 'xcb'

#-----------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

sys.path.append( os.path.abspath( os.path.join( os.path.dirname( __file__ ), '..', 'util' ) ) )

import make_range as mr


"""
Esercizio:
Grafico della funzione seno e del suo polinomio di taylor

note prof:
- fare la funzione per il factorial

note:
- per svilluppo cuttare y > 5
"""

# variabili globali ----------------------------------------------------------
ascisse = mr.range()

sinFunction = []
taylorPol = []

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
