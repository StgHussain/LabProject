import numpy as np
import scipy as scipy
import math
from Laguerre import Laguerre 

class LgBeam():

    def GenerateLGBeam(self, p, l, w):
        
        Xcords = np.linspace(-1, 1, 1024)
        Ycords = np.linspace(-1/1, 1/1, 1024)

        [rho, phi] = self.cart2pol(Xcords, Ycords)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        self.LaguerreBeam(p,l, 2*RhoSquaredOverWSquare)
    
    def LaguerreBeam(self, p, l, x):
        self.y = np.array(p + 1, 1)
        if p == 0:
            self.y = 1
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
        self.y = np.polyval(y, x)
        return self.y

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        print("lg Beam")

obj = LgBeam()
p = 0
l = 1
w = 0.12207
obj.GenerateLGBeam(p, l, w)
print (self.y)

