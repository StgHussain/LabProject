import numpy as np
import scipy as scipy
import math
from LgBeam import LgBeam

class LgHologram():

    def calcHologramGrid(self, pmat, lmat):
        print ("calc grid")
        self.N = [self.ySize, self.xSize]
        self.Intensity = np.zeros(self.N)
        #self.grid = self.Lmat.shape
        #this returns [1 1] in octave for some reason
        self.grid = [1, 1]
        self.points[0] = self.N[0]/self.grid[0]
        self.points[1] = self.N[1]/self.grid[1]
        self.range[0] = self.N[0]/min(self.N)
        self.range[1] = self.N[1]/min(self.N)

        self.Pmat[0] = pmat
        self.Pmat[1] = pmat

        Xcords = np.linspace(-self.range[0], self.range[1], self.points[0])
        Ycords = np.linspace(-self.range[1]/self.rowToCol, self.range[1]/self.rowToCol, self.points[1])
        self.FinalGrid = np.meshgrid(Xcords, Ycords)
        self.XX = self.FinalGrid [0]
        self.YY = self.FinalGrid [1]
        print ("end grid")

    def calculateIntensity(self, pMat, lMat, beamRad):
        print ("cal intensity")
        for i in range (1, self.grid[0]):
            for j in range (1, self.grid[1]):
                pMatVal = self.Pmat[i]
                lMatVal = lMat[i]
                beamRadVal = beamRad[i]
                xx = self.XX
                yy = self.YY
                LgBeamObj = LgBeam()
                self.Intensity[:,:,i,j] = LgBeamObj.GenerateLGBeam(pMatVal, lMatVal, beamRadVal, xx, yy)
        self.Intensity = np.reshape(self.Intensity, self.N)
        if self.normalize:
            R = abs(self.Intensity)
            R = R/max(max(self.Intensity))
            Phi = np.angle(self.Intensity)
            I = complex (0, 1)
            self.complexHologram = R * math.exp(I*Phi)
            normFactor = 1 / np.sum(np.sum(np.conjugate(self.complexHologram)*self.complexHologram))
        else:
            self.complexHologram = self.Intensity
            normFactor = 1
        return normFactor

    def generateHologram(self, Xsize, Ysize, PMatrix, lMatrix, beamRadiusPercent): #normalize and rowToCol required
        print ("gen holo")
        self.xSize = Xsize
        self.ySize = Ysize
        self.beamRad = beamRadiusPercent
        self.calcHologramGrid(PMatrix, lMatrix)
        normFactor = self.calculateIntensity(PMatrix, lMatrix, beamRadiusPercent)
        return normFactor, self.Intensity


    def __init__(self): # normalizeZeroOne, rowToCol):
        print ("hello")
        self.normalize = True
        self.rowToCol = 1
        self.points = [0, 0]
        self.range = [0, 0]
        self.Pmat = [0, 0]





