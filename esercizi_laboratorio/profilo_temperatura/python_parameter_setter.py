""" ----------------------------------------
Classe per il setting dei parametri

0 °C + 273,15 = 273,15 K
---------------------------------------- """

class ParameterSetter:
    
    def __init__(self):
        
        self.LunghezzaAsta = 2 #[m]
        self.Raggio = 0.001 #[m]
        
        self.TemperaturaA   = -20 #[°C] + 273.5 #[°K]
        self.TemperaturaB   = 40 #[°C] + 273.5  #[°K]
        self.TemperaturaAmb = 20 #[°C] + 273.5  #[°K]
        
        self.NumeroIntervalli = None
        
        self.constH = 100 #[W m^-2 K^-1]
        self.CapacitaTermica = 450 #[J Kg^-1 K^-1]
        self.DensitaAcciaio = 7.8 * 10**3 #[Kg m^-3]
        self.ConducibilitaTermica = 50 #[W m^-1 K^-1]
    
    
    def parameterSetter(self):
        
        print(" Inserire di seguito i parametri: ")
        
        print(" > Lunghezza asta [m] (consigliato 2): ")
        self.LunghezzaAsta = float( input("\t") )
        
        print(" > Raggio [m] (consigliato 0.001): ")
        self.Raggio = float( input("\t") )
        
        print(" > Temperatura estremo A [°C] (consigliato -20°C): ")
        self.TemperaturaA = float( input("\t") )
        #		self.TemperaturaA = self.TemperaturaA + 273.15
        
        print(" > Temperatura estremo B [°C] (consigliato 40°C): ")
        self.TemperaturaB = float( input("\t") )
        #		self.TemperaturaB = self.TemperaturaB + 273.15
        
        print(" > Temperatura ambiente [°C] (consigliato 20°C): ")
        self.TemperaturaAmb = float( input("\t") )
        #		self.TemperaturaAmb = self.TemperaturaAmb + 273.15
        
        print(" > Numero di intervalli: ")
        self.NumeroIntervalli = int( input("\t") )
    
    
#endclass

