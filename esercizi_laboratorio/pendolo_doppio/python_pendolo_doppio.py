#""" -----------------------------------------------------------------------
#Esercizio:
#propagazione del moto di un pendolo doppio con il metodo
#di Runge-Kutta a 4 punti
#
#Sistema di riferimento utilizzato:
#
# y	^
#	|
#  -----------------------------> x	
#	|\
#	| \ angolo 1, asta 1
#	|  \
#	|	* massa 1
#	|	:\ 
#	|   : \ angolo 2, asta 2
#	|   :  \
#	|       * massa 2
#	|
#
#Come variabili per il moto usiamo gli angoli
#La struttura vettoriale in cui conserviamo le variabili è:
#[ ang_1, ang_2, (d/dt)ang_1, (d/dt)ang_2 ]	
# il vettore forza è composto da: 
#[ (d/dt)ang_1, (d/dt)ang_2, (d2/dt2)ang_1, (d2/dt2)ang_2 ]
#----------------------------------------------------------------------- """

import sys
sys.path.append("/util/")

import numpy as np
import matplotlib.pyplot as plt

import python_parameter_setter as parameter_setter
import python_propagatore as propagatore


#set dei parametri del moto ------------------------------------------------
parameter_setter.parameterSetter(); #per usare i default commentare la riga

#definiamo il vettore di step zero
coordinateGeneralizzate0 = np.array([parameter_setter.ANGOLO_DISTACCO_1, parameter_setter.ANGOLO_DISTACCO_2, parameter_setter.VELOCITA_ANGOLARE_1, parameter_setter.VELOCITA_ANGOLARE_2])

#definiamo delle liste per la conservazione delle posizioni e dello step temporale
coordinateAngolo1 = []
coordinateAngolo2 = []
coordinateTemporali = []

#propaghiamo le equazioni del moto
indiceIterazione = 0
stepN0 = coordinateGeneralizzate0
stepN1 = np.zeros(4)

while( indiceIterazione <= parameter_setter.NUMERO_PASSI):
    
    stepN1 = propagatore.propagatoreRungeKutta4(stepN0)
    
    coordinateAngolo1.append( stepN1[0] )
    coordinateAngolo2.append( stepN1[1] )
    coordinateTemporali.append(indiceIterazione*parameter_setter.STEP_TEMPORALE)
    
    stepN0 = stepN1
    indiceIterazione+=1
    


#print(coordinateTemporali)
#print(coordinateAngolo1)
#print(coordinateAngolo2)


#restrizione all angolo 2pi
coordinateAngolo1Lim = []
coordinateAngolo2Lim = []

for element in coordinateAngolo1:
    
    dummy = element
    while(dummy > 2*np.pi):
        dummy -= (2*np.pi); 
    
    coordinateAngolo1Lim.append(dummy)

for element in coordinateAngolo2:
    
    dummy = element
    while(dummy > 2*np.pi):
        dummy -= (2*np.pi); 
    
    coordinateAngolo2Lim.append(dummy)



figure, ax = plt.subplots()
ax.plot( coordinateTemporali, coordinateAngolo1Lim)
ax.plot( coordinateTemporali, coordinateAngolo2Lim)
plt.grid()
plt.show()


