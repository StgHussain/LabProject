import numpy as np
import scipy as scipy
import math


class Laguerre():
    
    def GenerateBeam(self):
        pVal = self.p
        lVal = self.l
        y = np.array(pVal + 1, 1)
        if pVal == 0:
            y = 1
        else:
            for m in range (pVal):
                factM1 = math.factorial(pVal + 1)
                numerator = (np.power(-1, m)) * factM1
                factPM = math.factorial(pVal - m)
                factLM = math.factorial(lVal + m)
                factM2 = math.factorial(m)
                denom = factPM * factLM * factM2
                y = numerator/denom 

    def __init__(self, GivenP, GivenL, GivenX):
        self.p = GivenP
        self.l = GivenL
        self.x = GivenX