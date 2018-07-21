import numpy as np
import scipy as scipy
from Laguerre import Laguerre
import math

class LgBeam():

    #def GenerateLGBeam(self, p, l, w, xx, yy):
    def GenerateLGBeam(self, p, l, w):
        
        Xcords = np.linspace(-self.range[0], self.range[1], self.points[0])
        Ycords = np.linspace(-self.range[1]/self.rowToCol, self.range[1]/self.rowToCol, self.points[1])


        Pi = math.pi
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        factL = math.factorial (l)
        [rho, phi] = self.cart2pol(xx, yy)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        lag = Laguerre()
        LagResult = lag.LaguerreBeam(p, abs(l), 2*RhoSquaredOverWSquare)
        Clg = math.sqrt((2*factP/ (Pi * factLP))) / w
        imagNum = complex(0,-l*phi)
        Result = Clg * (self.SquareRoot2 * np.power(math.sqrt(RhoSquaredOverWSquare), abs(l))) * LagResult * math.exp(-RhoSquaredOverWSquare) * math.exp(imagNum)
        return Result

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        print (r)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        p = 0
        l = 1
        w = 0.12207
