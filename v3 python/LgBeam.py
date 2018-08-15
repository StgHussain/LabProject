import numpy as np
import cupy as cp
import math
import time
from Laguerre import Laguerre
from Utility import Utility
from AddGrating import Addgrating


class LgBeam():

    def GenerateLGBeam(self, p, l, w, sizePoints):
        n = sizePoints #change this to match grid sizeS
        XXcords = cp.linspace(-1, 1, sizePoints[1])
        YYcords = cp.linspace(-1/1, 1/1,  sizePoints[0]) #range/something (both need changing)
        Xcords, Ycords = cp.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)
        #[rho, phi] = self.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = cp.zeros((sizePoints[1], sizePoints[0]))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        tim1 = time.time()
        Values = self.LAG.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare)
        tim2 = time.time()
        print("time laguerre")
        print(tim2-tim1)

        #Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        Result = cp.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        imgNum = cp.multiply(phi, complex(0, -l))

        time1 = time.time()
       #Result calculation 
        RhoSqrt = cp.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = cp.power(RhoSqrt, abs(l))
        mult1 = cp.multiply(RhoSqrt, Values)
        mult2 = cp.multiply(cp.exp(-RhoSquaredOverWSquare), cp.exp(imgNum))
        Res2 = cp.multiply(mult1, mult2)
        Res2 = cp.multiply(Res2, Clg)
        Result = Res2
        #Results calculated 
        time2 = time.time()
        print("time numpy")
        print(time2 - time1)

        ResultNew = [cp.abs(number) for number in Result]
        maxResult = cp.amax(ResultNew)
        ResultNew = ResultNew/maxResult

        imaginaryNum = complex(0, 1)
        Phi = cp.angle(Result)
        Phi = cp.multiply(Phi, imaginaryNum)
        Phi = cp.exp(Phi)
        complexHologram = cp.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        complexHologram = cp.multiply(ResultNew, Phi) 
        #replace these with values specified by the user
        gratingAngle = 45
        gratingNum = 50
        ########################################################
        finalHologram = self.GRAT.addBlazedGrating(complexHologram, gratingAngle, gratingNum, sizePoints)
        #finalHologram = self.GRAT.selectGrating(self.gratingType, self,gratingVal, complexHologram, self.Grid)
        #return finalHologram
        self.UTIL.showImg(finalHologram)


    def __init__(self, p, l, w, grid):
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
        #first parameter is dimension y of grid, 8 not sure, 1 defined by laser used
        #w = self.UTIL.calculateBeamRad(1024, 8, 1)
        #need changes to calculate Beam Radius function 
        w = 0.12077
        self.GenerateLGBeam(p, l, w, grid)
        