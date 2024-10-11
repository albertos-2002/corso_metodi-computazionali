#global ---------------------
xMax = 4
NumeroPunti = 50000
OrdinePolinomio = 2

#internal ------------------
ascissePositive = []
ascisseNegative = []

#return --------------------
ascisse = []


def range(npFlag):
#go to default values

    if npFlag != "np":

        for index in range( NumeroPunti ):
            ascissePositive.append( xMax/NumeroPunti*index )

        for index in range( NumeroPunti -1, -1, -1 ):
            ascisseNegative.append( -ascissePositive[index] )

    if npFlag == "np":
        ascisse = range( NumeroPunti )
    
    ascisse = ascisseNegative + ascissePositive
        
    return ascisse


def ask_range():

    return ascisse




"""
doc:


utilizzando la funzione range in modo "più" complesso

le liste hanno indice che va da 0 a n-1
il primo termine si riferisce al valore max
il secondo termine è quello di stop NON INCLUSO
il terzo termine è quello di step

in questo modo creiamo un range che parte da n-1, decresci di una 
unità ad ogni interazione e si ferma a 0, comprendo in questo modo 
tutti gli elementi della lista in ordine inverso

#essendo l'intervallo simmetrico il risultato migliore si ha per x<25
#x=10 da un buon risultato

"""
