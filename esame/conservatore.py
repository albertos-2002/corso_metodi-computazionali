""" -------------------------------------------------------------------------
Classe per la conservazione dei dati calcolati
------------------------------------------------------------------------- """

class Conservatore:
    
    def __init__(self):
        
        self.vettorePrede = []
        self.vettorePredatori = []
        self.vettoreTempo = []
        
    #enddef
    
    def salvatoreSpaziale(self, vec):
        
        self.vettorePrede.append(vec[0])
        self.vettorePredatori.append(vec[1])
        
    #enddef
    
    def salvatoreTemporale(self, value):
        
        self.vettoreTempo.append(value)
        
    #enddef
    
#endclass

#creazione di istanza
consClass = Conservatore()

