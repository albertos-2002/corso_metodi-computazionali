import numpy as np
from scipy.constants import g as GRAVITA

import python_parameter_setter as parameter_setter

class Conservatore:
    
    def __init__(self, classeParametri = None):
        self.classPar = classeParametri
        
        self.coordinateAngolo1 = []
        self.coordinateAngolo2 = []
        self.velocitaAngolari1 = []
        self.velocitaAngolari2 = []
        
        self.coordinateTemporali = []
        
        self.cartesianoX1 = []
        self.cartesianoY1 = []
        self.cartesianoX2 = []
        self.cartesianoY2 = []
        
        self.energiaCinetica = []
        self.energiaPotenziale = []
        self.energiaTotale = []
        
        self.flagCartesiano = True
        self.flagEnergia = True
    
    
    def appendCooedinateGeneralizzate(self, coord = None):
        
        self.coordinateAngolo1.append( coord[0] )
        self.coordinateAngolo2.append( coord[1] )
        self.velocitaAngolari1.append( coord[2] )
        self.velocitaAngolari2.append( coord[3] )
    
    
    def appendTime(self, timeItem = None):
        self.coordinateTemporali.append(timeItem);	
    
    
    def cartesianatore(self):
        
        if(self.flagCartesiano):
            
            length = len(self.coordinateTemporali)
            
            for i in range(length):
                
                x1 = self.classPar.LUNGHEZZA_ASTA_1 \
                * np.sin( self.coordinateAngolo1[i] )
                y1 = - self.classPar.LUNGHEZZA_ASTA_1 \
                * np.cos( self.coordinateAngolo1[i] )
                
                x2 = self.classPar.LUNGHEZZA_ASTA_2 \
                * np.sin( self.coordinateAngolo2[i] )
                y2 = - self.classPar.LUNGHEZZA_ASTA_2 \
                * np.cos( self.coordinateAngolo2[i] );		
                
                self.cartesianoX1.append(x1)
                self.cartesianoY1.append(y1)
                self.cartesianoX2.append(x1+x2)
                self.cartesianoY2.append(y1+y2)
            
            
            self.flagCartesiano = False
        
    
    
    def energiatore(self):
        
        if(self.flagEnergia):
            
            length = len(self.coordinateTemporali)
            
            for i in range(length):
                
                dummyP1 = - ( self.classPar.MASSA_PARTICELLA_1 + self.classPar.MASSA_PARTICELLA_2 ) \
                * GRAVITA \
                * self.classPar.LUNGHEZZA_ASTA_1 \
                * np.cos( self.coordinateAngolo1[i] )
                dummyP2 = - self.classPar.MASSA_PARTICELLA_2 \
                * GRAVITA \
                * self.classPar.LUNGHEZZA_ASTA_2 \
                * np.cos( self.coordinateAngolo2[i] )
                self.energiaPotenziale.append(dummyP1 + dummyP2);			
                
                dummyC1 = 0.5 * self.classPar.MASSA_PARTICELLA_1 \
                * (self.classPar.LUNGHEZZA_ASTA_1**2) \
                * (self.velocitaAngolari1[i]**2)
                dummyC2 = 0.5 * self.classPar.MASSA_PARTICELLA_2 \
                * ( (self.classPar.LUNGHEZZA_ASTA_1 * self.velocitaAngolari1[i])**2 
                + (self.classPar.LUNGHEZZA_ASTA_2 * self.velocitaAngolari2[i])**2 )
                dummyC3 = self.classPar.MASSA_PARTICELLA_2 \
                * self.classPar.LUNGHEZZA_ASTA_1 \
                * self.classPar.LUNGHEZZA_ASTA_2 \
                * np.cos(self.coordinateAngolo1[i]-self.coordinateAngolo2[i]) \
                * self.velocitaAngolari1[i] \
                * self.velocitaAngolari2[i]
                self.energiaCinetica.append(dummyC1 + dummyC2 + dummyC3)
            
            
            self.energiaTotale = np.asarray(self.energiaPotenziale) \
            + np.asarray(self.energiaCinetica)
            
            self.flagEnergia = False
        
    
    
    
#endclass

