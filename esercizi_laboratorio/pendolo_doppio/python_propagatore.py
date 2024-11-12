""" -----------------------------------------------------------
Definizione delle funzioni di forza 

#La struttura vettoriale in cui conserviamo le variabili è:
#[ ang_1, ang_2, (d/dt)ang_1, (d/dt)ang_2 ]
# il vettore forza è composto da:
#[ (d/dt)ang_1, (d/dt)ang_2, (d2/dt2)ang_1, (d2/dt2)ang_2 ]
----------------------------------------------------------- """

from scipy.constants import g as GRAVITA; #[m/s^2]
import numpy as np

import python_parameter_setter as parameter_setter


def accelerazioneAngolare(vecCoordGen):
    
    vettoreAccelerazioni = np.zeros(2)
    
    sommaMasse = parameter_setter.MASSA_PARTICELLA_1 + parameter_setter.MASSA_PARTICELLA_2
    deltaAngoli = vecCoordGen[0] - vecCoordGen[1]
    deltaSeno = np.sin(deltaAngoli)
    deltaCoseno = np.cos(deltaAngoli)
    
    viola     = deltaCoseno**2
    #m2*l2*sin(theta1-theta1)*vel2^2
    rosso     = parameter_setter.MASSA_PARTICELLA_2 * parameter_setter.LUNGHEZZA_ASTA_2 * deltaSeno * (vecCoordGen[3]**2)
    #g*(m1+m2)*sin(theta1)
    azzurro   = GRAVITA * sommaMasse * np.sin(vecCoordGen[0])
    #m2*l1*sin(theta1-theta2)*vel1^2
    blu       = parameter_setter.MASSA_PARTICELLA_2 * parameter_setter.LUNGHEZZA_ASTA_1 * deltaSeno * (vecCoordGen[2]**2)
    #m2*g*sin(theta2)
    giallo    = parameter_setter.MASSA_PARTICELLA_2 * GRAVITA * np.sin(vecCoordGen[1])
    
    sommaRA = rosso + azzurro
    sommaBG = - blu + giallo
    
    dummyDen1 = parameter_setter.LUNGHEZZA_ASTA_1 * ( parameter_setter.MASSA_PARTICELLA_1 + parameter_setter.MASSA_PARTICELLA_2*(1-viola) )
    vettoreAccelerazioni[0] = (-1/dummyDen1) * ( sommaRA - deltaCoseno*sommaBG )
    
    dummyDen2 = parameter_setter.LUNGHEZZA_ASTA_2 * ( parameter_setter.MASSA_PARTICELLA_2 - ( (parameter_setter.MASSA_PARTICELLA_2**2)/sommaMasse )*viola )
    vettoreAccelerazioni[1] = (-1/dummyDen2) * ( ( -parameter_setter.MASSA_PARTICELLA_2*deltaCoseno/sommaMasse )*sommaRA + sommaBG )
    
    return vettoreAccelerazioni


def forza(vecCoordGen):
    
    vecForza = np.zeros(4)
    accelerazioni = accelerazioneAngolare(vecCoordGen)
    
    vecForza[0] = vecCoordGen[2]
    vecForza[1] = vecCoordGen[3]
    vecForza[2] = accelerazioni[0]
    vecForza[3] = accelerazioni[1]
    
    return vecForza


def propagatoreRungeKutta4(formerStep):
    
    halfTime = parameter_setter.STEP_TEMPORALE / 2
    sixthTime = parameter_setter.STEP_TEMPORALE / 6
    
    #intermedio 1
    intermedio1 = formerStep
    #intermedio 2
    forza1 = forza(intermedio1)
    intermedio2 = formerStep + forza1*halfTime
    #intermedio 3
    forza2 = forza(intermedio2)
    intermedio3 = formerStep + forza2*halfTime
    #intermedio 4
    forza3 = forza(intermedio3)
    intermedio4 = formerStep + forza3*parameter_setter.STEP_TEMPORALE
    
    #step finale
    nextStep = formerStep + ( forza1 + 2*(forza2 + forza3) + forza(intermedio4) )*sixthTime
    
    return nextStep


