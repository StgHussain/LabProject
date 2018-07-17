import numpy as np
import scipy as scipy
import math
from Laguerre import Laguerre

class LgBeam():

    def GenerateLGBeam(self, p, l, w, xx, yy):
        [rho, phi] = self.cart2pol(xx, yy)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        lag = Laguerre()
        LagResult = lag.LaguerreBeam(p, abs(l), 2*RhoSquaredOverWSquare)
        

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.x = 0