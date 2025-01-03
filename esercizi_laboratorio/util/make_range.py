#global keyword -> permette di modificare la variabile globale (quelle definite sopra)
import numpy as np

#global ----------------------------------------------------------------------------------------------------
xMax = 4
NumeroPunti = 50000
step = 2*xMax/NumeroPunti; 
#il fattore 2 deriva dal fatto che l'intervallo viene simmetrizato
#step = DeltaX / numeroPunti = 2*xMax / numeroPunti 
#infatti il range di valori spazia tra -xMax e xMax  

#internal ---------------------
ascissePositive = []
ascisseNegative = []

#return -----------------------
ascisse = []

# ----------------------------------------------------------------------------------------------------------

def range_man():
    #usa i valori predefiniti
    global ascissePositive, ascisseNegative, ascisse
    
    #il lato positivo contiene la metà (simmetria) dei punti totali
    for index in range( int(NumeroPunti*0.5) ):
        ascissePositive.append( step*index )
    
    
    
    """
    il primo termine si riferisce al valore max (start)
    il secondo termine è quello di stop NON INCLUSO 
    il terzo termine è quello di step
    
    in questo modo creiamo un range che parte da n-1, decresce di una   
    unità ad ogni interazione e si ferma a 0, comprendo in questo modo 
    tutti gli elementi della lista in ordine inverso
    """
    #prende le ascisse positive e le copia rovesciate e cambiate di segno
    for index in range( ( int(NumeroPunti*0.5) ) -1, -1, -1 ):
        ascisseNegative.append( -ascissePositive[index] )
    
    
    ascisse = ascisseNegative + ascissePositive
    return ascisse


def range_np():
    
    global ascisse
    
    ascisse = np.arange(-xMax, xMax, step)
    return ascisse


def ask_range(npFlag):
    
    global xMax, NumeroPunti, step
    
    xMax            = float( input("Inserire il valore di xMax:") ) 
    NumeroPunti     =   int( input("Inserire il numero di punti:") ) 
    
    step = 2*xMax/NumeroPunti
    
    if npFlag == "np": range_np()
    if npFlag != "np": range_man()
    
    return ascisse


