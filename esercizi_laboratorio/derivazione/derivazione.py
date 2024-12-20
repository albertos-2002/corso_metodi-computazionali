""" ---------------------------------------------------------------------------------
Esercizio:
Derivazione con il metodo delle differenze finite
Modificare il programma fornito dal docente per calcolare l’errore nella derivata
prima della funzione sin(x) risultante dall’uso delle formule O(h), 0(h^2), O(h^4).

L’errore va riportato su di un grafico.

Fissati gli estremi dell'intervallo, spingendo il numero di punti verso infinito
l'algoritmo riporta risultati non aspettati
--------------------------------------------------------------------------------- """

import sys
sys.path.append("../util/")
#------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.gridspec as gridspec

import make_range as mr
import set_graph as sg

#global -----------------------------------------------------------	
ascisse = mr.ask_range("np")

fSeno   = np.sin(ascisse)
fCoseno = np.cos(ascisse); #derivata "esatta"	

derivataOrdineh1 = [] 
derivataOrdineh2 = [] 
derivataOrdineh4 = [] 
errOrdineh1 = [] 
errOrdineh2 = [] 
errOrdineh4 = [] 

#calcolo derivate -------------------------------------------------
h = mr.step

#ordine h1
for index in range( len(ascisse)-2 ):
    #l'ultimo valore deve essere un i+1, -2 per la non inclusività dello stop
    result = (fSeno[index+1]-fSeno[index]) / h; 
    derivataOrdineh1.append( result )
    errOrdineh1.append( fCoseno[index]-result )


#ordine h2
for index in range( 1, len(ascisse)-2 ):
    #primo valore i-1, ultimo i+1
    result = (fSeno[index+1] - fSeno[index-1]) / (2*h)
    derivataOrdineh2.append( result );	
    errOrdineh2.append( fCoseno[index]-result )


#ordine h4
for index in range( 2, len(ascisse)-3 ):
    #primo valore i-2, ultimo i+2
    dummyDen = 12*h
    dummy1 = fSeno[index+1] - fSeno[index-1]
    dummy2 = fSeno[index-2] - fSeno[index+2]
    result = (8*dummy1 + dummy2) / dummyDen
    derivataOrdineh4.append( result )
    errOrdineh4.append( fCoseno[index]-result )


#grafica ------------------------------------------------------------------------------------------------------------------
# Create a figure
figure = plt.figure()

# Define a gridspec with 2 rows and 3 columns
gs = gridspec.GridSpec(2, 3, figure=figure)

# Create subplots 
graph_main        = figure.add_subplot(gs[0, 0]);  # Row 0, columns 0
graph_zoom        = figure.add_subplot(gs[0, 1]);  # Row 1, column 1
graph_zoomzoom    = figure.add_subplot(gs[0, 2]);  # Row 1, column 2

graph_allerr      = figure.add_subplot(gs[1, 0]);  # Row 0, column 0
graph_zoomerr     = figure.add_subplot(gs[1, 1]);  # Row 1, column 1
graph_zoomzoomerr = figure.add_subplot(gs[1, 2]);  # Row 1, column 2


sg.set_style( fontSize=19, markerSize=1 )

graph_main.set_title("Seno e derivate")
graph_main.set_ylabel( "f($\\theta$) e f\'($\\theta$)" ); 
graph_main.set_xlabel("Angolo")
graph_main.plot( ascisse, fSeno,   linestyle="-", color="b" ,label="Seno" )
graph_main.plot( ascisse, fCoseno, linestyle="-", color="k" ,label="Derivata" )
graph_main.plot( ascisse[:-2],  derivataOrdineh1, linestyle="--", color="g" ,label=r"$\mathcal{O}(h)$" )
graph_main.plot( ascisse[1:-2], derivataOrdineh2, linestyle="--", color="r" ,label=r"$\mathcal{O}(h^2)$" )
graph_main.plot( ascisse[2:-3], derivataOrdineh4, linestyle="--", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_main)

# zoom dinamico
CosenoMenoSeno = np.abs(fCoseno - fSeno)
indexIntersezione = np.argmin(CosenoMenoSeno);  #determina una delle intersezioni
valoreAscissa  = ascisse[indexIntersezione]
valoreOrdinata = fCoseno[indexIntersezione]
indexErrh1Min = np.argmax( errOrdineh1 );  #trova l'indice del massimo valore di errore
indexErrh2Min = np.argmax( errOrdineh2 )

graph_zoom.set_title("Seno e derivate (zoom)")
graph_zoom.set_ylabel( "f($\\theta$) e f\'($\\theta$)" )
graph_zoom.set_xlabel("Angolo")
graph_zoom.set_ylim( valoreOrdinata - errOrdineh1[indexErrh1Min], valoreOrdinata + errOrdineh1[indexErrh1Min] )
graph_zoom.set_xlim( valoreAscissa - errOrdineh1[indexErrh1Min], valoreAscissa + errOrdineh1[indexErrh1Min] )
graph_zoom.plot( ascisse, fSeno,   linestyle="-", color="b" ,label="Seno" )
graph_zoom.plot( ascisse, fCoseno, linestyle="-", color="k" ,label="Derivata" )
graph_zoom.plot( ascisse[:-2],  derivataOrdineh1, linestyle="--", color="g" ,label=r"$\mathcal{O}(h)$" )
graph_zoom.plot( ascisse[1:-2], derivataOrdineh2, linestyle="--", color="r" ,label=r"$\mathcal{O}(h^2)$" )
graph_zoom.plot( ascisse[2:-3], derivataOrdineh4, linestyle="--", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_zoom)

graph_zoomzoom.set_title("Seno e derivate (zoom)")
graph_zoomzoom.set_ylabel( "f($\\theta$) e f\'($\\theta$)" )
graph_zoomzoom.set_xlabel("Angolo")
graph_zoomzoom.set_ylim( valoreOrdinata - errOrdineh2[indexErrh2Min], valoreOrdinata + errOrdineh2[indexErrh2Min] )
graph_zoomzoom.set_xlim( valoreAscissa - errOrdineh2[indexErrh2Min], valoreAscissa + errOrdineh2[indexErrh2Min] )
#graph_zoomzoom.plot( ascisse, fSeno,   linestyle="-", color="b" ,label="Seno" )
graph_zoomzoom.plot( ascisse, fCoseno, linestyle="-", color="k" ,label="Derivata" )
graph_zoomzoom.plot( ascisse[1:-2], derivataOrdineh2, linestyle="--", color="r" ,label=r"$\mathcal{O}(h^2)$" )
graph_zoomzoom.plot( ascisse[2:-3], derivataOrdineh4, linestyle="--", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_zoomzoom)


graph_allerr.set_title("Errore")
graph_allerr.set_ylabel("Errore")
graph_allerr.set_xlabel("Angolo")
graph_allerr.plot( ascisse[:-2],  errOrdineh1, linestyle="", marker=".", color="g" ,label=r"$\mathcal{O}(h)$" )
graph_allerr.plot( ascisse[1:-2], errOrdineh2, linestyle="", marker=".", color="r" ,label=r"$\mathcal{O}(h^2)$" )
graph_allerr.plot( ascisse[3:-2], errOrdineh4, linestyle="", marker=".", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_allerr)

graph_zoomerr.set_title("Errore")
graph_zoomerr.set_ylabel("Errore")
graph_zoomerr.set_xlabel("Angolo")
graph_zoomerr.plot( ascisse[1:-2], errOrdineh2, linestyle="", marker=".", color="r" ,label=r"$\mathcal{O}(h^2)$" )
graph_zoomerr.plot( ascisse[3:-2], errOrdineh4, linestyle="", marker=".", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_zoomerr)

graph_zoomzoomerr.set_title("Errore")
graph_zoomzoomerr.set_ylabel("Errore")
graph_zoomzoomerr.set_xlabel("Angolo")
graph_zoomzoomerr.plot( ascisse[3:-2], errOrdineh4, linestyle="", marker=".", color="m" ,label=r"$\mathcal{O}(h^4)$" )
sg.make_fine(graph_zoomzoomerr)

plt.show()

