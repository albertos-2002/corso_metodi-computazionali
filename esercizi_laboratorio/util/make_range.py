import numpy as np

#global ---------------------
#buon risultato per ordini bassi del polinomio
xMax = 4
NumeroPunti = 50000

#internal ------------------
#le liste hanno indice che va da 0 a n-1
ascissePositive = []
ascisseNegative = []

#return --------------------
ascisse = []

#global keyword -> permette di modificare la variabile globale (quelle definite sopra)

def range_man():
    #go to default values
    global ascissePositive, ascisseNegative, ascisse
    
    for index in range( NumeroPunti ):
        ascissePositive.append( xMax/NumeroPunti*index )
    
    
    #prende le ascisse positive e le copia rovesciate e cambiate di segno
    """
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
    return ascisse


def range_np():
    
    global ascisse
    
    ascisse = np.arange(-xMax, xMax, 2*xMax/NumeroPunti)
    return ascisse


def ask_range(npFlag):
    
    global xMax, NumeroPunti, OrdinePolinomio
    
    xMax            = float( input("Inserire il valore di xMax:") ) 
    NumeroPunti     =   int( input("Inserire il numero di punti:") ) 
    
    if npFlag == "np": range_np()
    if npFlag != "np": range_man()
    
    return ascisse


