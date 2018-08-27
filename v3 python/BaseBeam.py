import numpy as np
import math
from Utility import Utility
from AddGrating import Addgrating

class BaseBeam():

    def __init__(self):
        #pass in parameters 
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        self.UTIL = Utility()
        self.GRAT = Addgrating()

    def defineParams(self, gratingType, gratingAngle, gratingNum, gridXY, p, l):

        #self.gratingType = gratingType
        self.gratingAngle = gratingAngle
        self.gratingNum = gratingNum
        self.Grid = gridXY
        self.P = p
        self.L = l
        self.w = self.UTIL.calculateBeamRad(gridXY[1], 8, 1)#grid, pixel size, beam rad
        self.generateMeshGrid(gridXY)
      
    def generateMeshGrid(self, gridXY):
        XXcords = np.linspace(-1, 1, gridXY[1])
        YYcords = np.linspace(-1/1, 1/1,  gridXY[0]) #range/something (both need changing)
        self.Xcords, self.Ycords = np.meshgrid(XXcords, YYcords)

    def addGrating(self, finalHologram):
        finalHologram = self.GRAT.addBlazedGrating(complexHologram, gratingAngle, gratingNum, sizePoints)
        #finalHologram = self.GRAT.selectGrating(self.gratingType, self,gratingVal, complexHologram, self.Grid)

    