""" -------------------------------------------
Plotting dei dati per il pendolo

calcolo cartesiano ed energetico da spostare
------------------------------------------- """
import sys
sys.path.append("../util/")

import matplotlib.pyplot as plt

import python_conservatore as conservatore
import set_graph as sg


class DataPlotter:
    
    def __init__(self, argConservatore = None):
        #sg.set_style(fontSize=12, markerSize=1)
        self.conservatore = argConservatore
    
    
    def plotAngolo(self):
        
        figure, ax = plt.subplots()
        
        ax.set_title("Variazione angolo in funzione dello step temporale")
        ax.set_ylabel("Angoli [rad]")
        ax.set_xlabel("Step temporale [s]")
        
        ax.plot( self.conservatore.coordinateTemporali, 
        self.conservatore.coordinateAngolo1, 
        linestyle="--", label="Angolo 1")
        ax.plot( self.conservatore.coordinateTemporali, 
        self.conservatore.coordinateAngolo2, 
        linestyle="--", label="Angolo 2")
        
        sg.make_fine(ax)
        plt.show(block=False)
    
    
    
    def plotCartesiano(self):
        
        self.conservatore.cartesianatore()
        
        figure, ax = plt.subplots()
        
        ax.set_title("Coordinate cartesiane")
        ax.set_ylabel("Coordinata Y [m]")
        ax.set_xlabel("Coordinata X [m]")
        
        ax.plot( self.conservatore.cartesianoX1, 
        self.conservatore.cartesianoY1, 
        linestyle="--", label="Angolo 1")
        ax.plot( self.conservatore.cartesianoX2, 
        self.conservatore.cartesianoY2, 
        linestyle="--", label="Angolo 2")
        
        sg.make_fine(ax)
        plt.show(block=False)
    
    
    
    def plotEnergia(self):
        
        self.conservatore.energiatore()
        
        figure, ax = plt.subplots()
        
        ax.set_title("Energia meccanica in funzione del tempo (teoricamente conservata)")
        ax.set_ylabel("Energia [J]")
        ax.set_xlabel("Tempo [s]")
        
        ax.plot(self.conservatore.coordinateTemporali, 
        self.conservatore.energiaTotale, 
        linestyle="--", label="Energia totale")
        
        #sg.make_fine(ax)
        plt.grid()
        plt.show(block=False);		
    
    
#endclass

