import numpy as np
import math
from Laguerre import Laguerre
from BeamParams import BeamParams
from Utility import Utility
from AddGrating import Addgrating


class LgBeam():

    def GenerateLGBeam(self, p, l, w, sizePoints):
        XXcords = np.linspace(-1, 1, sizePoints[1])
        YYcords = np.linspace(-1/1, 1/1,  sizePoints[0]) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((sizePoints[1], sizePoints[0]))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        Values = self.LAG.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare)

        #Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        Result = np.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        imgNum = np.multiply(phi, complex(0, -l))

       #Result calculation 
        RhoSqrt = np.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = np.power(RhoSqrt, abs(l))
        mult1 = np.multiply(RhoSqrt, Values)
        mult2 = np.multiply(np.exp(-RhoSquaredOverWSquare), np.exp(imgNum))
        Res2 = np.multiply(mult1, mult2)
        Res2 = np.multiply(Res2, Clg)
        Result = Res2
        #Results calculated 

        ResultNew = [np.abs(number) for number in Result]
        maxResult = np.amax(ResultNew)
        ResultNew = ResultNew/maxResult

        imaginaryNum = complex(0, 1)
        Phi = np.angle(Result)
        Phi = np.multiply(Phi, imaginaryNum)
        Phi = np.exp(Phi)
        complexHologram = np.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        complexHologram = np.multiply(ResultNew, Phi) 
        return complexHologram
        
        
    def returnBeam(self):
        return self.result
        
    def __init__(self, BeamParam):
        self.p = BeamParam.getP()
        self.l = BeamParam.getL()
        self.grid = BeamParam.getGrid()
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        
        self.LAG = Laguerre()
        self.UTIL = Utility()
        w = 0.12077 ############################## still need to change this
        
        self.result = self.GenerateLGBeam(self.p, self.l, w, self.grid)
       

        