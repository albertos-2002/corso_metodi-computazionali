""" ---------------------------------------------------------
Esercizio:
Grafico della funzione seno e del suo polinomio di taylor
--------------------------------------------------------- """

import sys
sys.path.append("../util/")
#-----------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import math

import make_range as mr
import set_graph as sg


# variabili globali ----------------------------------------------------------
ascisse = mr.ask_range("man")
sinFunction = []
taylorPol = []

#calcolo della funzione seno -----------------------------------------------
for element in ascisse:
    sinFunction.append( np.sin(element) )


#polinomio di taylor ------------------------------------------------------
""" ----------------------------------------------------------------------
Ricordiamo la formula della serie di taylor (maclaurin) per il seno
serie n=0 to n=inf of (-1)^n / (2n+1)! x^(2n+1)
---------------------------------------------------------------------- """
for element in ascisse:
    dummy = 0
    for n in range(mr.OrdinePolinomio+1): #arriviamo così fino ad ordine n e non n-1
        dummyExp = 2*n +1
        dummy += (-1)**n / math.factorial( dummyExp ) * element**dummyExp
    
    taylorPol.append(dummy)


#creazione del grafico ("metodo colab notebook") ---------------------------
figure, ax = plt.subplots()

ax.plot( ascisse, sinFunction, linestyle="--", color="orange", label="Sen Function" )
ax.plot( ascisse, taylorPol, linestyle=(0, (1, 5)), color="green", label="Taylor seriess" )
ax.set_ylim(-1.5, 1.5); #rende visibile il grafico per ogni ordine del polinomio
ax.set_title( "Seno e polinomio di taylor" )
ax.set_xlabel( "Angolo" )
ax.set_ylabel( "Seno" )
sg.make_fine(ax)

plt.show()

