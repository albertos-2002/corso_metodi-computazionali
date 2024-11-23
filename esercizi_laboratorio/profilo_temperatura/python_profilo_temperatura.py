""" -------------------------------------------------------
Calcolo del profilo di temperatura di una asta metallica
------------------------------------------------------- """
import sys
sys.path.append("../util/")

import numpy as np
import matplotlib.pyplot as plt

#import set_grahp as sg

import python_parameter_setter as parameter_setter
import python_integratore as integratore
import python_data_plotter as data_plotter

SetOfPar = parameter_setter.ParameterSetter()
Integratore = integratore.EdoCondizioniContorno( classPar = SetOfPar)


SetOfPar.parameterSetter()

Integratore.TheOneToCallToIntegrate()


plotter = data_plotter.DataPlotter( param=SetOfPar, integratore=Integratore)
plotter.plotTemp()

