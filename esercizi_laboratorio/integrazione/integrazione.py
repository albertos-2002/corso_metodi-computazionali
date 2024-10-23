""" -------------------------------------------------------
Esercizio:
integrazione di e^x tra 0 e 1 (risulstato e-1) con:
- rettangoli naif
- rettangoli
- trapezi
- simpson
variare N 
graficare errore in scala bilogaritmica
ax.semilogx()
ax.semilogy()
------------------------------------------------------- """

import sys 
sys.path.append("../util/")
#------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

import set_graph as sg

debugFlag = True
#global -----------------------------------------------------------
OrdiniDivisione = []

risultatoEsatto = np.e -1
estremoInferiore = 0
estremoSuperiore = 1

#conserviamo i risultati in una lista ordinata come gli ordini di divisione
risultatiRettangoliNaif = []
risultatiRettangoli     = []
risultatiTrapezi        = []
risultatiSimpson        = []

errRettangoliNaif = []
errRettangoli     = []
errTrapezi        = []
errSimpson        = [];  

# ------------------------------------------
numeroEsponenti = int( input("numero ordini di grandezza (10**) da spaziare: \n") )
for ordine in range(1, numeroEsponenti+1, 1):
    OrdiniDivisione.append( 10**ordine )

## -----------
if debugFlag:
    print("\n")
    print("Esponenti per gli ordini N in cui su divide l'intervallo")
    print(OrdiniDivisione)
    print("\n")
    input()

## ------------


for numeroPunti in OrdiniDivisione:
    
    step = (estremoSuperiore - estremoInferiore) / numeroPunti
    puntiGriglia = np.arange( estremoInferiore, estremoSuperiore, step )
    
    if len(puntiGriglia) % 2 != 0:
        print("Numero di punti totali è dispari")
        input()
    
    
    # RETTANGOLI NAIF -------------------------------------------------------
    #considera come valore di f in h l'estremo sinistro
    #ci fermiamo a n-1 elementi
    sommaRettangoliNaif = 0
    for index in range( len(puntiGriglia) ):
        valoreFunzione = np.e ** puntiGriglia[index]
        sommaRettangoliNaif += valoreFunzione*step
    
    risultatiRettangoliNaif.append( sommaRettangoliNaif )
    errRettangoliNaif.append( abs(risultatoEsatto - sommaRettangoliNaif) )
    ## -----------
    if debugFlag:
        print("\n")
        print("Ordine attuale")
        print(numeroPunti)
        print("Errore rettangoli naif")
        print( abs(risultatoEsatto - sommaRettangoliNaif) )
        print("\n")
    
    ## ------------
    
    # RETTANGOLI ------------------------------------------------------------
    #consideriamo il valore centrale dell' intervallo h
    #range fino a len-1, range restituisce argmax-1 e dobbia arrivare al penultimo punti considerando indice di lista
    sommaRettangoli = 0
    for index in range( len(puntiGriglia)-1 ):
        valoreEsponente = ( puntiGriglia[index+1] + puntiGriglia[index] ) /2
        valoreFunzione = np.e ** valoreEsponente
        sommaRettangoli += valoreFunzione*step
    
    risultatiRettangoli.append( sommaRettangoli )
    errRettangoli.append( abs(risultatoEsatto - sommaRettangoli) )
    ## -----------
    if debugFlag:
        print("\n")
        print("Ordine attuale")
        print(numeroPunti)
        print("Errore rettangoli")
        print( abs(risultatoEsatto - sommaRettangoli) )
        print("\n")
    
    ## ------------
    
    # TRAPEZI ---------------------------------------------------------------
    #consideriamo la retta che passa per i due estremi dell'intervallo h
    sommaTrapezi = 0
    for index in range( len(puntiGriglia)-1 ):
        valoreFunzione_1 = np.e ** puntiGriglia[index]
        valoreFunzione_2 = np.e ** puntiGriglia[index+1]
        sommaTrapezi += (valoreFunzione_1 + valoreFunzione_2) * step / 2
    
    risultatiTrapezi.append( sommaTrapezi )
    errTrapezi.append( abs(risultatoEsatto - sommaTrapezi) )
    ## -----------
    if debugFlag:
        print("\n")
        print("Ordine attuale")
        print(numeroPunti)
        print("Errore trapezi")
        print( abs(risultatoEsatto - sommaTrapezi) )
        print("\n")
    
    ## ------------
    
    # SIMPSON ---------------------------------------------------------------
    #consideriamo un polinomio di ordine 2 in un intervallo 2h
    sommaSimpson = 0
    for index in range( 1, len(puntiGriglia)-1 ): #non include l'ultimo punto e il primo delle ascisse
        
        if index % 2 == 0: #punti di indice pari
            sommaSimpson += ( (2/3) * np.e ** puntiGriglia[index] ) * step
        
        else: #restanti punti di indice dispari
            sommaSimpson += ( (4/3) * np.e ** puntiGriglia[index] ) * step
        
    
    #punti di bordo
    sommaSimpson += (1/3) * np.e ** puntiGriglia[1]
    sommaSimpson += (1/3) * np.e ** puntiGriglia[-1]
    
    risultatiSimpson.append( sommaSimpson )
    errSimpson.append( abs(risultatoEsatto - sommaSimpson) )
    ## -----------
    if debugFlag:
        print("\n")
        print("Ordine attuale")
        print(numeroPunti)
        print("Errore simpson")
        print( abs(risultatoEsatto - sommaSimpson) )
        print("\n")
        input()
    
    ## ------------
    


## -----------
if debugFlag:
    print("\n")
    input()
    print("\n")

## ------------

# GRAFICA --------------------------------------------------

figure , axs = plt.subplots(nrows=2, ncols=1)

sg.set_style(fontSize=19, markerSize=10)

axs[0].set_title("Grafico errore (log)")
axs[0].set_ylabel("$|\\ valoreEsatto - valoreCalcolato\\ |$")
axs[0].set_xlabel("Ordini di grandezza")
axs[0].semilogy()
axs[0].semilogx()
axs[0].plot( OrdiniDivisione, errRettangoliNaif, marker="x", linestyle=":", label=r'Rettangoli Naif $\mathcal{O}(h)$')
axs[0].plot( OrdiniDivisione, errRettangoli,     marker="x", linestyle=":", label=r'Rettangoli $\mathcal{O}(h^2)$')
axs[0].plot( OrdiniDivisione, errTrapezi,        marker="x", linestyle=":", label=r'Trapezi $\mathcal{O}(h^2)$')
axs[0].plot( OrdiniDivisione, errSimpson,        marker="x", linestyle=":", label=r'Simpson $\mathcal{O}(h^4)$')
sg.make_fine(axs[0])

axs[1].set_title("Grafico errore")
axs[1].set_ylabel("$|\\ valoreEsatto - valoreCalcolato\\ |$")
axs[1].set_xlabel("Ordini di grandezza")
axs[1].plot( OrdiniDivisione, errRettangoliNaif, marker="x", linestyle=":", label=r'Rettangoli Naif $\mathcal{O}(h)$')
axs[1].plot( OrdiniDivisione, errRettangoli,     marker="x", linestyle=":", label=r'Rettangoli $\mathcal{O}(h^2)$')
axs[1].plot( OrdiniDivisione, errTrapezi,        marker="x", linestyle=":", label=r'Trapezi $\mathcal{O}(h^2)$')
axs[1].plot( OrdiniDivisione, errSimpson,        marker="x", linestyle=":", label=r'Simpson $\mathcal{O}(h^4)$')
sg.make_fine(axs[1])

plt.show()

