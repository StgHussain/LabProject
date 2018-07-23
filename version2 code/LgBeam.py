import numpy as np
import scipy as scipy
import math
from Laguerre import Laguerre 

class LgBeam():

    def GenerateLGBeam(self, p, l, w):
        
        Xcords = np.linspace(-1, 1, 1024)
        Ycords = np.linspace(-1/1, 1/1, 1024) #range/something (both need changing)
        print("co ordinates done")
        [rho, phi] = self.cart2pol(Xcords, Ycords)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        print(RhoSquaredOverWSquare)
        Values = self.LaguerreBeam(p,l, 2*RhoSquaredOverWSquare)
        print (w)

        Pi = math.pi
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (Pi * factLP))) / w
        Result = []
        for i in range (1024):
            imagNum = complex(0,-l*phi[i])
            reqVal = Values[i]
            Result.append(Clg * (self.SquareRoot2 * np.power(math.sqrt(RhoSquaredOverWSquare[i]), abs(l))) * reqVal * np.exp(-RhoSquaredOverWSquare[i]) * np.exp(imagNum))
        return Result
    
    def LaguerreBeam(self, p, l, x):
        #self.y = np.array(p + 1, 1)
        print ("laguerre")
        #Vals = [2]
        Vals = []
        if p == 0:
            Vals = [1] * 1024
        else:
            for m in range (p):
                factM1 = math.factorial(p + 1)
                numerator = (np.power(-1, m)) * factM1
                factPM = math.factorial(p - m)
                factLM = math.factorial(l + m)
                factM2 = math.factorial(m)
                denom = factPM * factLM * factM2
                Vals.append(numerator/denom)
        #polyVal if needed
        PolyCoeff = Vals
        #PolyCoeff = np.polyval(Vals, x)
        return PolyCoeff

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


