import numpy as np
import scipy as scipy
import math


class Laguerre():
    
    def LaguerreBeam(self, p, l, x):
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
                y[p + l - m] = numerator/denom 
        #polyVal if needed
        #y = np.polyval(y, x)
        print (y)
        return y
        
    def __init__(self):
        print ("start")