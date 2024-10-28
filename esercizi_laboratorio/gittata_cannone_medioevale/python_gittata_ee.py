""" -----------------------------------------------------------------------------------------
Gittata del cannone medioevale con il metodo di eulero esplicito:


definiamo la struttura del vettore coordinate generalizzate e della forza generalizzata
coordinate generalizzate
[spazio x,   spazio y,   velocità x, valocità y]
forza generalizzata
[velocità x, velocità y, forza x,    forza y]

Il sistema di riferimento lo definiamo come 

y^
|
|
|
|
----------------------->
|                   x  

velocità di partenza sono positive
----------------------------------------------------------------------------------------- """

import sys
sys.path.append("../util/")

import numpy as np

# Costanti ----------------------------------------------------------------------------------------------------
RAGGIO_PROIETTILE = 0.05; #[m]
DENSITA_PROIETTILE = 2.7; #[g/cm^3]
AREA_SEZIONE_TRASVERSALE = np.pi * RAGGIO_PROIETTILE**2; #[m^2]

DENSITA_ARIA = 1.22; #[kg/m^3]
COEFFICIENTE_RESISTENZA_AERODINAMICA_SFERA = 0.47

from scipy.constants import g as GRAVITA; #[m/s^2]

#parametri consigliati
VELOCITA_INIZIALE = 100; #[m/s]
ANGOLO_LANCIO = np.pi/4; #[rad]
STEP_TEMPORALE = 0.001; #[s]

#calcoliamo la massa del proiettile
MASSA_PROIETTILE = DENSITA_PROIETTILE * (4/3) * np.pi * ((RAGGIO_PROIETTILE*100)**3) / 1000; #[Kg]

# ------------------------------------------------------------------------------------------------------------------------------------------------

#calcoliamo la gittata ideale (senza attrito)
gittataIdeale = 2 * (VELOCITA_INIZIALE**2) * np.sin(ANGOLO_LANCIO) * np.cos(ANGOLO_LANCIO) / GRAVITA

#diamo le condizioni iniziali
coordinateGeneralizzate_0 = np.array( [0, 0, VELOCITA_INIZIALE*np.cos(ANGOLO_LANCIO), VELOCITA_INIZIALE*np.sin(ANGOLO_LANCIO)] )

#definiamo il modulo della forza di attrito
moduloForzaAttrito = 0.5 * DENSITA_ARIA * COEFFICIENTE_RESISTENZA_AERODINAMICA_SFERA * AREA_SEZIONE_TRASVERSALE * (VELOCITA_INIZIALE**2)

# ------------------------------------------------------------------------------------------------------------------------------------------------

gittataAttritoEuleroEsplicito = 0

# definiamo il metodo di eulero esplicito

def calcolatoreEuleroEsplicito(vecCoordGen):
    
    NextStep = np.zeros(4)
    NextStep[0] = vecCoordGen[2]
    NextStep[1] = vecCoordGen[3]
    NextStep[2] = - moduloForzaAttrito * np.cos(ANGOLO_LANCIO) / MASSA_PROIETTILE
    NextStep[3] = - GRAVITA + (moduloForzaAttrito * np.sin(ANGOLO_LANCIO) / MASSA_PROIETTILE)
    
    return NextStep*STEP_TEMPORALE


gittataFlag = False

#applicazione del metodo di eulero esplicito
coordinateStep_0 = coordinateGeneralizzate_0
coordinateStep_1 = np.zeros(4)

while (not gittataFlag):
    
    coordinateStep_1 = coordinateStep_0 + calcolatoreEuleroEsplicito(coordinateStep_0)
    
    #metodo della bisezione - controlliamo il cambio di segno della coordinata y
    if( coordinateStep_1[1]*coordinateStep_0[1] < 0 ):
        #retta passante per 2 punti con condizione y=0
        gittataAttritoEuleroEsplicito = coordinateStep_0[0] - coordinateStep_0[1] * ( coordinateStep_1[0] - coordinateStep_0[0] ) / ( coordinateStep_1[1] - coordinateStep_0[1] )
        gittataFlag = True
    
    
    #setting del nuovo punto di partenza
    coordinateStep_0 = coordinateStep_1 
    coordinateStep_1 = np.zeros(4)


print(" Gittata teorica senza attrito [m]:")
print(" ", gittataIdeale)
print("\n Gittata calcolata con il metodo di eulero esplicito con attrito:")
print(" ", gittataAttritoEuleroEsplicito)


