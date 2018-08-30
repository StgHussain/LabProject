import numpy as np
import math
from Laguerre import Laguerre
from Utility import Utility


class LgBeam():

    def Generate(self):
        XXcords = np.linspace(-1, 1, self.grid[1])
        YYcords = np.linspace(-1/1, 1/1,  self.grid[0]) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((self.grid[1], self.grid[0]))
        RhoSquaredOverWSquare = (rho*rho)/(self.w*self.w)
        Values = self.LAG.LaguerreBeam(self.p, self.l, 2*RhoSquaredOverWSquare)

        #Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)
        factP = math.factorial(self.p)
        factLP = math.factorial(abs(self.l) + self.p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / self.w

        Result = np.zeros((self.grid[0], self.grid[1]), dtype=complex)
        imgNum = np.multiply(phi, complex(0, -self.l))

       #Result calculation 
        RhoSqrt = np.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = np.power(RhoSqrt, abs(self.l))
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
        complexHologram = np.zeros((self.grid[0], self.grid[1]), dtype=complex)
        complexHologram = np.multiply(ResultNew, Phi) 
        self.result = complexHologram
        
    def setGrid(self, newGrid):
        self.grid = newGrid
        
    def returnBeam(self):
        return self.result
        
    def __init__(self, p, l, beamWidth):
        self.p = p
        self.l = l
        self.beamWidth = beamWidth
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        
        self.LAG = Laguerre()
        self.UTIL = Utility()
        self.w = 0.12077 ############################## still need to change this
        
       

        