import numpy as np
import scipy as scipy
import math


class Laguerre():
    
    @classmethod
    def LaguerreBeam(cls, p, l, x):
        y = np.array(p + 1, 1)
        if p == 0:
            y = 1
        else:
            for m in range (p):
                factM1 = math.factorial(p + 1)
                numerator = (np.power(-1, m)) * factM1
                factPM = math.factorial(p - m)
                factLM = math.factorial(l + m)
                factM2 = math.factorial(m)
                denom = factPM * factLM * factM2
                y = numerator/denom 
                return y

    def __init__(self):
        self.y = 0