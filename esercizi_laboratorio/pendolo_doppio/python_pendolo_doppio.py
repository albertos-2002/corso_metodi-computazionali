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
#	|        * massa 2
#	|
#
#Come variabili per il moto usiamo gli angoli
#La struttura vettoriale in cui conserviamo le variabili è:
#[ ang_1, ang_2, (d/dt)ang_1, (d/dt)ang_2 ]	
# il vettore forza è composto da: 
#[ (d/dt)ang_1, (d/dt)ang_2, (d2/dt2)ang_1, (d2/dt2)ang_2 ]
#----------------------------------------------------------------------- """

import sys
sys.path.append("../util/")

import numpy as np

import python_parameter_setter as parameter_setter
import python_propagatore as propagatore
import python_data_plotter as data_plotter
import python_conservatore as conservatore
import python_animator as animator


#creiamo una instanza della classe che setta i parametri iniziali
SetOfPar1 = parameter_setter.ParameterSetter()
SetOfPar1.parameterSetter()
coordinateGeneralizzate0 = SetOfPar1.coordinateGeneralizzate0

#classe per conservare le propagazioni
conservatore1 = conservatore.Conservatore( classeParametri=SetOfPar1 )

#classe per il plotting dei dati e animazione
dataPlotter1 = data_plotter.DataPlotter( argConservatore=conservatore1 )
animator1 = animator.Animator(dataArg = conservatore1)


#propaghiamo le equazioni del moto
indiceIterazione = 0
stepN0 = coordinateGeneralizzate0
stepN1 = np.zeros(4)


while( indiceIterazione <= SetOfPar1.NUMERO_PASSI):
    
    propagatoreMoto = propagatore.Propagatore( classeParametri = SetOfPar1,
    vettoreCoordinateSV = stepN0 )
    stepN1 = propagatoreMoto.propagatoreRungeKutta4()
    
    conservatore1.appendCooedinateGeneralizzate( coord = stepN1 )
    conservatore1.appendTime( timeItem = indiceIterazione*SetOfPar1.STEP_TEMPORALE )
    
    stepN0 = stepN1
    indiceIterazione+=1



#plotting delle coordinate (punto4)
#dataPlotter1.plotAngolo()
#dataPlotter1.plotCartesiano()
#dataPlotter1.plotEnergia()
animator1.giveLife()

input("Enter to close plot and exit ....")

