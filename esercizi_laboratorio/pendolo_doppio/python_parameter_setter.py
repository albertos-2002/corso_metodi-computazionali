""" ------------------------------------------------
Setting dei parametri per il moto
------------------------------------------------ """
import numpy as np

MASSA_PARTICELLA_1  = 1
MASSA_PARTICELLA_2  = 1
LUNGHEZZA_ASTA_1    = 1
LUNGHEZZA_ASTA_2    = 1
ANGOLO_DISTACCO_1   = np.deg2rad(179)
ANGOLO_DISTACCO_2   = np.deg2rad(179)
VELOCITA_ANGOLARE_1 = 0
VELOCITA_ANGOLARE_2 = 0
STEP_TEMPORALE      = 0.001
NUMERO_PASSI        = 10000

def parameterSetter():
    
    global MASSA_PARTICELLA_1,MASSA_PARTICELLA_2,LUNGHEZZA_ASTA_1,LUNGHEZZA_ASTA_2,ANGOLO_DISTACCO_1,ANGOLO_DISTACCO_2,VELOCITA_ANGOLARE_1,VELOCITA_ANGOLARE_2,STEP_TEMPORALE,NUMERO_PASSI
    
    print(" Inserire nella sezione seguente i parametri per il moto: ")
    
    print(" > Massa delle particelle [kg] (consigliato 1): ")
    MASSA_PARTICELLA_1 = float( input("    massa 1:\t") )
    MASSA_PARTICELLA_2 = float( input("    massa 2:\t") )
    
    print(" > Lunghezza delle aste [m] (consigliato 1): ")
    LUNGHEZZA_ASTA_1 = float( input("    asta 1:\t") )
    LUNGHEZZA_ASTA_2 = float( input("    asta 2:\t") )
    
    print(" > Angolo di distacco [°] (consigliato 179°): ")
    ANGOLO_DISTACCO_1 = float( input("    angolo 1:\t") )
    ANGOLO_DISTACCO_2 = float( input("    angolo 2:\t") )
    
    ANGOLO_DISTACCO_1 = np.deg2rad(ANGOLO_DISTACCO_1)
    ANGOLO_DISTACCO_2 = np.deg2rad(ANGOLO_DISTACCO_2)
    
    print(" > Velocità angolare iniziale [...] (consigliato 0): ")
    VELOCITA_ANGOLARE_1 = float( input("    velocità 1:\t") )
    VELOCITA_ANGOLARE_2 = float( input("    velocita 2:\t") )
    
    print(" > Step temporale [s] (consigliato 0.001): ")
    STEP_TEMPORALE = float( input("\t\t") )
    
    print(" > Passi temporali (consigliato 10k): ")
    NUMERO_PASSI = float( input("\t\t") )
    


