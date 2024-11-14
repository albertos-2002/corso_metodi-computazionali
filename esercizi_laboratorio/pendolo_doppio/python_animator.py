""" ---------------------------------------------------
Classe per la gestione delle animazioni
--------------------------------------------------- """
import sys
sys.path.append("../util/")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import set_graph as sg
import python_conservatore as conservatore

class Animator:
    
    def __init__(self, dataArg = None):
        self.data = dataArg
        self.frameN = 0
        
        self.figure, self.ax = plt.subplots()
        
        self.ax.set_xlim(-2.5,2.5)
        self.ax.set_ylim(-2.6,2.5)
        self.ax.set_title("Animazione")
        self.ax.set_xlabel("Posizione X [m]")
        self.ax.set_ylabel("Posizione Y [m]")
        
        #masse e perno del pendolo
        self.pivot, = self.ax.plot( [], [], markersize=5, color="gray", marker="o", zorder=2)
        self.massa1, = self.ax.plot( [], [], markersize=9, color="r", marker="o", label="Massa 1", zorder=2)
        self.massa2, = self.ax.plot( [], [], markersize=9, color="g", marker="o", label="Massa 2", zorder=2)
        
        #aste di collegamento
        self.rod1, = self.ax.plot( [], [], color="lightgray", linestyle="-", lw=3, zorder=1)
        self.rod2, = self.ax.plot( [], [], color="lightgray", linestyle="-", lw=3, zorder=1)
        
        #coordinate oggetti
        self.pivotX = 0
        self.pivotY = 0
        self.massa1X = 0
        self.massa1Y = 0
        self.massa2X = 0
        self.massa2Y = 0
        
        #traccia per le masse
        self.traccia1, = self.ax.plot( [], [], color="r", alpha=0.4, linestyle=":", lw=2)
        self.traccia2, = self.ax.plot( [], [], color="g", alpha=0.4, linestyle=":", lw=2)
        self.tracciaLenght = 150
        
        self.sliceLower = 0
        self.traccia1X = 0
        self.traccia1Y = 0
        self.traccia2X = 0
        self.traccia2Y = 0
        
        #traccia totale
        self.totalTraccia1, = self.ax.plot( [], [], color="r", alpha=0.20, linestyle=":", lw=1)
        self.totalTraccia2, = self.ax.plot( [], [], color="g", alpha=0.30, linestyle=":", lw=1)
        self.totalTraccia1X = 0
        self.totalTraccia1Y = 0
        self.totalTraccia2X = 0
        self.totalTraccia2Y = 0
        
        #progressbar
        self.progressBar = plt.Rectangle( (-2, -2.3), 0, 0.06, color="dodgerblue", alpha=0.7, zorder=2)
        self.ax.add_patch(self.progressBar)
        self.progress = 0
        
        self.backgroundBar = plt.Rectangle( (-2, -2.3), 4, 0.06, color="slategray", alpha=0.6, zorder=1 )
        self.ax.add_patch(self.backgroundBar)
        
        self.animazione = None
    
    
    def init(self):
        self.pivot.set_data( self.pivotX, self.pivotY )
        self.massa1.set_data([],[])
        self.massa2.set_data([],[])
        self.rod1.set_data([],[])
        self.rod2.set_data([],[])
        self.traccia1.set_data([],[])
        self.traccia2.set_data([],[])
        self.totalTraccia1.set_data([],[])
        self.totalTraccia2.set_data([],[])
        
        return self.pivot, self.massa1, self.massa2, self.rod1, self.rod2, \
        self.traccia1, self.traccia2, self.totalTraccia1, self.totalTraccia2
    
    
    def update(self, frame):
        
        self.massa1X = self.data.cartesianoX1[frame]
        self.massa1Y = self.data.cartesianoY1[frame]
        self.massa2X = self.data.cartesianoX2[frame]
        self.massa2Y = self.data.cartesianoY2[frame]
        
        self.sliceLower = max(0, frame - self.tracciaLenght)
        self.traccia1X = self.data.cartesianoX1[self.sliceLower : frame+1]
        self.traccia1Y = self.data.cartesianoY1[self.sliceLower : frame+1]
        self.traccia2X = self.data.cartesianoX2[self.sliceLower : frame+1]
        self.traccia2Y = self.data.cartesianoY2[self.sliceLower : frame+1]
        
        self.totalTraccia1X = self.data.cartesianoX1[0 : frame+1]
        self.totalTraccia1Y = self.data.cartesianoY1[0 : frame+1]
        self.totalTraccia2X = self.data.cartesianoX2[0 : frame+1]
        self.totalTraccia2Y = self.data.cartesianoY2[0 : frame+1]
        
        self.progress = frame / self.frameN
        
        #update per le masse
        self.massa1.set_data(self.massa1X, self.massa1Y)
        self.massa2.set_data(self.massa2X, self.massa2Y)
        
        #update per la traccia
        self.traccia1.set_data(self.traccia1X, self.traccia1Y)
        self.traccia2.set_data(self.traccia2X, self.traccia2Y)
        
        self.totalTraccia1.set_data(self.totalTraccia1X, self.totalTraccia1Y)
        self.totalTraccia2.set_data(self.totalTraccia2X, self.totalTraccia2Y)
        
        #update per le aste
        self.rod1.set_data( [self.pivotX, self.massa1X], [self.pivotY, self.massa1Y] )
        self.rod2.set_data( [self.massa1X, self.massa2X], [self.massa1Y, self.massa2Y] )
        
        #update per la progress bar
        self.progressBar.set_width(4*self.progress);		
        
        return self.pivot, self.massa1, self.massa2, self.rod1, self.rod2, self.traccia1, \
        self.traccia2, self.progressBar, self.totalTraccia1, self.totalTraccia2
    
    
    def giveLife(self):
        
        self.data.cartesianatore()
        self.frameN = len(self.data.coordinateTemporali)
        
        self.animazione = FuncAnimation( self.figure,
        self.update,
        frames=self.frameN,
        init_func = self.init,
        blit = True,
        interval = 1)
        
        sg.make_fine(self.ax)
        
        self.animazione.save("animation.gif", writer="imagemagick", fps=1000)
        
        plt.show(block=False)
    
    
    
#endclass

