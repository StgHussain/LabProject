import numpy as np
import scipy as scipy
import math
from Laguerre import Laguerre

class LgBeam():

    def GenerateLGBeam(self, p, l, w, xx, yy):
        Pi = math.pi
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        factL = math.factorial (l)
        [rho, phi] = self.cart2pol(xx, yy)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        lag = Laguerre()
        LagResult = lag.LaguerreBeam(p, abs(l), 2*RhoSquaredOverWSquare)
        Clg = math.sqrt((2*factP/ (Pi * factLP))) / w
        Result = Clg * (self.Square2 * np.power(math.sqrt(RhoSquaredOverWSquare), abs(l))) * LagResult * math.exp(-RhoSquaredOverWSquare) * exp(j * l * phi)
        

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.x = 0
        self.Square2 = math.sqrt(2)