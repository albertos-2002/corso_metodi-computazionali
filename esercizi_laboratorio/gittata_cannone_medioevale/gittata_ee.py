""" -----------------------------------------------------------------------------------------
Gittata del cannone medioevale con il metodo di eulero esplicito:

definiamo la struttura del vettore coordinate generalizzate e della forza generalizzata
coordinate generalizzate:
[spazio x,   spazio y,   velocità x, valocità y]
forza generalizzata:
[velocità x, velocità y, forza x,    forza y]

Il sistema di riferimento lo definiamo come:

y^
|
|
|
---------------->
|            x  
----------------------------------------------------------------------------------------- """

import sys
sys.path.append("../util/")

import numpy as np
import matplotlib.pyplot as plt
import set_graph as sg

# Costanti ----------------------------------------------------------------------------------------------------
RAGGIO_PROIETTILE = 0.05; #[m]
DENSITA_PROIETTILE = 2.7; #[g/cm^3]
AREA_SEZIONE_TRASVERSALE = np.pi * RAGGIO_PROIETTILE**2; #[m^2]

DENSITA_ARIA = 1.22; #[kg/m^3]
COEFFICIENTE_RESISTENZA_AERODINAMICA_SFERA = 0.47

from scipy.constants import g as GRAVITA; #[m/s^2]

#calcoliamo la massa del proiettile
MASSA_PROIETTILE = DENSITA_PROIETTILE * (4/3) * np.pi * ((RAGGIO_PROIETTILE*100)**3) / 1000; #[Kg]

# -----------------------------------------------------------------------------------------------------------------------------------------------

#richiesta dei parametri
print(" Inserire di seguito i parametri: ")

print(" velocità iniziale [m/s] (consigliato 100): ")
VELOCITA_INIZIALE = float( input("  ") )

print(" angolo di lancio [deg] (consigliato 45): ")
ANGOLO_LANCIO =     float( input("  ") )

print(" step temporale [s] (consigliato 0.001): ")
STEP_TEMPORALE =    float( input("  ") )

print(" considerare forza di attrito [true/false]: ")
flagAttritoStr = input("  ")
FLAG_ATTRITO = True if flagAttritoStr=="true" else False

ANGOLO_LANCIO = np.deg2rad(ANGOLO_LANCIO)

# ------------------------------------------------------------------------------------------------------------------------------------------------
#calcoliamo la gittata ideale (senza attrito)
if (not FLAG_ATTRITO):
    gittataIdeale = 2 * (VELOCITA_INIZIALE**2) * np.sin(ANGOLO_LANCIO) * np.cos(ANGOLO_LANCIO) / GRAVITA


#diamo le condizioni iniziali
coordinateGeneralizzate_0 = np.array( [0, 0, VELOCITA_INIZIALE*np.cos(ANGOLO_LANCIO), VELOCITA_INIZIALE*np.sin(ANGOLO_LANCIO)] )

# ------------------------------------------------------------------------------------------------------------------------------------------------

gittataAttritoEuleroEsplicito = 0
stepXEuleroEsplicito = []
stepYEuleroEsplicito = []

stepXEuleroEsplicito.append( coordinateGeneralizzate_0[0] )
stepYEuleroEsplicito.append( coordinateGeneralizzate_0[1] )

# definiamo il metodo di eulero esplicito
def calcolatoreEuleroEsplicito(vecCoordGen):
    
    NextStep = np.zeros(4)
    NextStep[0] = vecCoordGen[2]
    NextStep[1] = vecCoordGen[3]
    
    if(FLAG_ATTRITO):
        
        #modulo della forza di attrito
        forzaAttritoX = 0.5 * DENSITA_ARIA * COEFFICIENTE_RESISTENZA_AERODINAMICA_SFERA * AREA_SEZIONE_TRASVERSALE * ( vecCoordGen[2]**2)
        forzaAttritoY = 0.5 * DENSITA_ARIA * COEFFICIENTE_RESISTENZA_AERODINAMICA_SFERA * AREA_SEZIONE_TRASVERSALE * ( vecCoordGen[3]**2)
        
        #per il nostro SdR
        #per una velocità positiva -> attrito con segno negativo
        #per una velocità negativa -> attrito con seno positivo
        
        if( vecCoordGen[2] >= 0 ):
            NextStep[2] = - forzaAttritoX / MASSA_PROIETTILE
        
        else:
            NextStep[2] = + forzaAttritoX / MASSA_PROIETTILE
        
        
        if( vecCoordGen[3] >= 0 ):
            NextStep[3] = - GRAVITA - forzaAttritoY / MASSA_PROIETTILE
        
        else:
            NextStep[3] = - GRAVITA + forzaAttritoY / MASSA_PROIETTILE
        
    
    else:
        
        NextStep[2] = - 0
        NextStep[3] = - GRAVITA
    
    
    return NextStep*STEP_TEMPORALE


#applicazione del metodo di eulero esplicito ---------------------------------------------------------------------------------------------------------------------
gittataFlag = False
contatoreIterazione = 0
listaIterazione = [0]

coordinateStep_0 = coordinateGeneralizzate_0
coordinateStep_1 = np.zeros(4)

while (not gittataFlag):
    
    contatoreIterazione += 1
    listaIterazione.append(contatoreIterazione)
    
    coordinateStep_1 = coordinateStep_0 + calcolatoreEuleroEsplicito(coordinateStep_0)
    
    stepXEuleroEsplicito.append( coordinateStep_1[0] )
    stepYEuleroEsplicito.append( coordinateStep_1[1] )
    
    #metodo della bisezione - controlliamo il cambio di segno della coordinata y
    if( coordinateStep_1[1]*coordinateStep_0[1] < 0 ):
        #retta passante per 2 punti con condizione y=0
        gittataAttritoEuleroEsplicito = coordinateStep_0[0] - coordinateStep_0[1] * ( coordinateStep_1[0] - coordinateStep_0[0] ) / ( coordinateStep_1[1] - coordinateStep_0[1] )
        gittataFlag = True
    
    
    #setting del nuovo punto di partenza
    coordinateStep_0 = coordinateStep_1 
    coordinateStep_1 = np.zeros(4)
    


#traiettoria analitica (moto senza attrito) per punti ------------------------------------------------------------------------------------------------------
if(not FLAG_ATTRITO):
    soluzioneAnaliticaX = []
    soluzioneAnaliticaY = []
    
    for stepMoltiplicatore in listaIterazione:
        tempo = STEP_TEMPORALE * stepMoltiplicatore
        
        dummyX = (VELOCITA_INIZIALE*np.cos(ANGOLO_LANCIO)*tempo) + coordinateGeneralizzate_0[0]
        dummyY = (-0.5*GRAVITA*(tempo**2)) + (VELOCITA_INIZIALE*np.sin(ANGOLO_LANCIO)*tempo) + coordinateGeneralizzate_0[1]
        
        soluzioneAnaliticaX.append( dummyX )
        soluzioneAnaliticaY.append( dummyY )
    


#risultati e grafica -----------------------------------------------------------------------------------------------------------------------------------------
if (not FLAG_ATTRITO):
    print("\n Gittata teorica [m]:")
    print(" ", gittataIdeale)


if(not FLAG_ATTRITO):
    print("\n Gittata calcolata con il metodo di eulero esplicito [m]:")
    print(" ", gittataAttritoEuleroEsplicito)

else:
    print("\n Gittata calcolata con il metodo di eulero esplicito con attrito [m]:")
    print(" ", gittataAttritoEuleroEsplicito);	


print("\n Itarazioni necessarie:")
print(" ", listaIterazione[-1])

figure, ax = plt.subplots()
sg.set_style(fontSize=19, markerSize=1)

ax.set_title("Curva di moto con metodo di eulero esplicito ")
ax.set_xlabel("Coordinata x $[m]$")
ax.set_ylabel("Coordinata y $[m]$")

if(not FLAG_ATTRITO):
    ax.plot(soluzioneAnaliticaX, soluzioneAnaliticaY, marker="x", linestyle="", color="orange", label="Traiettoria analitica")


ax.plot(stepXEuleroEsplicito, stepYEuleroEsplicito, marker="x", linestyle="", color="g", label="Traiettoria eulero esplicito")
sg.make_fine(ax)

plt.show()

