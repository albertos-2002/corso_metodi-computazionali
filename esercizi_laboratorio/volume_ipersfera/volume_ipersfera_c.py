""" -------------------------------------------------------------------------------
------------------------------------------------------------------------------- """
import numpy as np
import scipy

def main():
    
    dimensioneSpazio = 1
    numeroPunti = 1
    
    stimaVolumeSfera = 0
    valoreTeoricoIntegrale = 0
    volumeIpercubo = 0
    
    probabilita = 0
    incertezzaVolume = 0
    
    puntiInterniSfera = 0
    
    puntiX = 0
    
    rng = np.random.default_rng()
    
    #set dei parametri --------------------------------------------------------------------------------------------
    print(" Inserire di seguito i parametri per il calcolo:\n")
    print(" > Dimensione dello spazio:")
    dimensioneSpazio = int(input("\t"))
    print("\n > Numero di punti:")
    numeroPunti = int(input("\t"))
    
    
    #calcoliamo il valore teorico per l'integrale -----------------------------------------------------------------
    numeratore = np.pi ** (dimensioneSpazio/2)
    denominatore = scipy.special.gamma( (dimensioneSpazio/2)+1 )
    valoreTeoricoIntegrale = numeratore / denominatore
    
    print("\n Risultato teorico per l'integrale di volume di una ipersfera:")
    print("\t", valoreTeoricoIntegrale)
    
    
    #calcolo integrale con monte carlo ------------------------------------------------------------------------------------------------
    volumeIpercubo = 2**dimensioneSpazio
    
    for _ in range(numeroPunti):
        puntiX = 2 * rng.random( size=dimensioneSpazio, dtype=np.float64 ) -1; #numeri casuali tra -1 e 1
        
        if (np.dot(puntiX,puntiX) < 1):
            puntiInterniSfera = puntiInterniSfera + 1
        
        puntiX = 0
    
    
    probabilita = puntiInterniSfera / numeroPunti
    stimaVolumeSfera = probabilita * volumeIpercubo
    
    
    #incertezza sul metodo ------------------------------------------------------------------------------------------------------
    incertezzaVolume = volumeIpercubo * np.sqrt( ( probabilita * (1-probabilita) ) / numeroPunti )
    
    
    #print dei risultati --------------------------------------------------------------------------------------------------------
    print("\n Risultato del calcolo con monte carlo per la stima di volume:")
    print("\t", stimaVolumeSfera)
    
    print("\n Ordine accuratezza del metodo (dipende dal numero di punti):")
    print("\t", 1/np.sqrt(numeroPunti) )
    
    print("\n Incertezza del risultato:")
    print("\t", incertezzaVolume);	
    
#enddef

if __name__ == "__main__":
    main()


