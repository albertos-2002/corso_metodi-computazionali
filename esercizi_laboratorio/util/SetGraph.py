""" ----------------------------------
Classe per rifinire la grafica dei
grafici prodotti durante il corso
---------------------------------- """

import matplotlib.pyplot as plt

class SetGraph:
    
    def __init__(self):
        pass
    #enddef
    
    @staticmethod
    def makeFine(axObj):
        
        #disegno degli assi
        axObj.axhline( 0, color='grey', linestyle=(0, (1, 3)) );  # Horizontal axis
        axObj.axvline( 0, color='grey', linestyle=(0, (1, 3)) );  # Vertical axis
        
        axObj.legend()
        axObj.grid()
        
        return axObj
    #enddef
    
    @staticmethod
    def setStyle(fontSize=10, markerSize=6, smallLegend=False, bigAxT=False):
        
        plt.rcParams['axes.titlesize']  = fontSize;      # Set title size
        
        if bigAxT:
            plt.rcParams['axes.labelsize']  = fontSize+7;    # Set label size	
        
        if smallLegend:
            plt.rcParams['legend.fontsize'] = fontSize-4;	
        
        
        plt.rcParams['lines.markersize'] = markerSize;  # Reset to the default value
        
        plt.tight_layout()
        
        # Enable LaTeX rendering
        plt.rcParams['text.usetex'] = False
        
        return
    #enddef
    
#endclass

