import numpy as np
import math
import time
import matplotlib.pyplot as plt
from Laguerre import Laguerre
from Utility import Utility
from AddGrating import Addgrating


class LgBeam():

    def GenerateLGBeam(self, p, l, w, sizePoints):
        n = sizePoints #change this to match grid sizeS
        XXcords = np.linspace(-1, 1, sizePoints)
        YYcords = np.linspace(-1/1, 1/1,  sizePoints) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)
        #[rho, phi] = self.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((n, n))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        Values = self.LAG.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)
        #Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)

        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        Result = np.zeros((n, n), dtype=complex)
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
        complexHologram = np.zeros((n, n), dtype=complex)
        complexHologram = np.multiply(ResultNew, Phi) 
        #replace these with values specified by the user
        gratingAngle = 45
        gratingNum = 50
        ###################################################
        finalHologram = self.GRAT.addBlazedGrating(complexHologram, gratingAngle, gratingNum, sizePoints)
        #finalHologram = self.GRAT.selectGrating(self.gratingType, self,gratingVal, complexHologram, self.Grid)
        self.UTIL.showImg(finalHologram)


    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        #when this beam type is called all the values and parameters will be set in this function
        #self.gratingType = 
        #self.gratingVal[0] = gratingAngle
        #self.gratingVal[1] = gratingNum
        #self.Grid = gridXY
        self.LAG = Laguerre()
        self.UTIL = Utility()
        self.GRAT = Addgrating()
        