#global ---------------------
#buon risultato per ordini bassi del polinomio
xMax = 4
NumeroPunti = 50000
OrdinePolinomio = 2

#internal ------------------
ascissePositive = []
ascisseNegative = []

#return --------------------
ascisse = []


def range_man():
    #go to default values
    
    for index in range( NumeroPunti ):
        ascissePositive.append( xMax/NumeroPunti*index )
    
    
    for index in range( NumeroPunti -1, -1, -1 ):
        ascisseNegative.append( -ascissePositive[index] )
    
    
    ascisse = ascisseNegative + ascissePositive
    return ascisse


def range_np():
    
    ascisse = ascisseNegative + ascissePositive
    return ascisse


def ask_range():
    
    range_man()
    return ascisse



""" -----------------------------------------------------------------------
doc:

utilizzando la funzione range in modo "più" complesso

le liste hanno indice che va da 0 a n-1
il primo termine si riferisce al valore max
il secondo termine è quello di stop NON INCLUSO
il terzo termine è quello di step

in questo modo creiamo un range che parte da n-1, decresci di una 
unità ad ogni interazione e si ferma a 0, comprendo in questo modo 
tutti gli elementi della lista in ordine inverso
----------------------------------------------------------------------- """

