import numpy as np
import math
import time
from Laguerre import Laguerre
from Utility import Utility
from AddGrating import Addgrating
from BaseBeam import BaseBeam


class LgBeam(BaseBeam):

    def GenerateLGBeam(self, p, l, w, sizePoints):
        n = sizePoints #change this to match grid sizeS
        XXcords = np.linspace(-1, 1, sizePoints[1])
        YYcords = np.linspace(-1/1, 1/1,  sizePoints[0]) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)
        #[rho, phi] = self.cart2pol(Xcords, Ycords)

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
        #replace these with values specified by the user
        gratingAngle = 45
        gratingNum = 50
        ########################################################
        finalHologram = self.GRAT.addBlazedGrating(complexHologram, gratingAngle, gratingNum, sizePoints)
        #finalHologram = self.GRAT.selectGrating(self.gratingType, self,gratingVal, complexHologram, self.Grid)
        #return finalHologram
        #self.UTIL.showImg(finalHologram)


    def __init__(self, p, l, w, grid, gratingType, gratingAngle, gratingNum):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        baseBeam = BaseBeam()
        baseBeam.defineParams(gratingType, gratingAngle, gratingNum, grid, p, l)
        #when this beam type is called all the values and parameters will be set in this function
        #self.gratingType = 
        #self.gratingVal[0] = gratingAngle
        #self.gratingVal[1] = gratingNum
        #self.Grid = gridXY 


        self.LAG = Laguerre()
        self.UTIL = Utility()
        self.GRAT = Addgrating()
        #first parameter is dimension y of grid, 8 not sure, 1 defined by laser used
        #w = self.UTIL.calculateBeamRad(1024, 8, 1)
        #need changes to calculate Beam Radius function 
        w = 0.12077
        self.GenerateLGBeam(p, l, w, grid)
        