""" ---------------------------------------------------
Classe per la gestione delle animazioni
--------------------------------------------------- """

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import conservatore

class Animator:
    
    def __init__(self, dataArg = None):
        self.data = dataArg
        
        self.figure, self.ax = plt.subplots()
        
        #masse e perno del pendolo
        self.pivot, = self.ax.plot( [], [], markersize=5, color="gray", markerstyle="o")
        self.massa1, = self.ax.plot( [], [], markersize=10, color="r", markerstyle="o")
        self.massa2, = self.ax.plot( [], [], markersize=10, color="g", markerstyle="o")
        
        #aste di collegamento
        self.rod1, = self.ax.plot( [], [], color="lightgray", linestyle="-")
        self.rod2, = self.ax.plot( [], [], color="lightgray", linestyle="-")
        
        #coordinate oggetti
        self.pivotX = 0
        self.pivotY = 0
        self.massa1X = 0
        self.massa1Y = 0
        self.massa2X = 0
        self.massa2Y = 0
    
    
    def init(self):
        self.pivot.set_data( self.pivotX, self.pivotY )
        self.massa1.set_data([],[])
        self.massa2.set_data([],[])
        self.rod1.set_data([],[])
        self.rod2.set_data([],[])
        
        return self.pivot, self.massa1, self.massa2, self.rod1, self.rod2
    
    
    def update(self, frame):
        
        self.massa1X = self.data.cartesianoX1[frame]
        self.massa1Y = self.data.cartesianoY1[frame]
        self.massa2X = self.data.cartesianoX2[frame]
        self.massa2Y = self.data.cartesianoY2[frame]
        
        #update per le masse
        self.massa1.set_data(self.massa1X, self.massa1Y)
        self.massa2.set_data(self.massa2X, self.massa2Y)
        
        #update per le aste
        self.rod1.set_data( [self.pivotX, self.massa1X], [self.pivotY, self.massa1Y] )
        self.rod2.set_data( [self.massa1X, self.massa2X], [self.massa1Y, self.massa2Y] )
        
        return self.pivot, self.massa1, self.massa2, self.rod1, self.rod2
    
    
    def giveLife(self):
        
        frames = len(self.data.coordinateTemporali)
        
        animazione = FuncAnimation( self.figure,
        self.update,
        frames,
        init_func = self.init,
        blit = True,
        interval = 10)
        
        plt.show(block=False);	
    
    
    
#endclass

