import numpy as np
import scipy as scipy
import math
from LgBeam import LgBeam

class LgHologram():

    def calcHologramGrid(self):
        self.N = [self.ySize, self.xSize]
        self.Intensity = np.zeros[self.N]
        self.grid = self.Lmat.shape
        self.Intensity = np.zeros[self.N]
        self.points = self.N/self.grid
        self.range = self.N/min(self.N)
        self.Pmat[1:self.grid(1), 1:self.grid(2)] = self.Pmat
        Xcords = np.linspace(-self.range(1), self.range(1), self.points(1))
        Ycords = np.linspace(-self.range(2)/self.rowToCol, range(2)/self.rowToCol, self.points(2))
        self.FinalGrid = np.meshgrid(Xcords, Ycords)
        self.XX = self.FinalGrid [0]
        self.YY = self.FinalGrid [1]

    def calculateIntensity(self, pMat, lMat, beamRad):
        for i in range (1, self.grid(1)):
            for j in range (1, self.grid(2)):
                pMatVal = self.Pmat[i, j]
                lMatVal = self.Lmat[i,j]
                beamRadVal = beamRad[i,j]
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
        self.xSize = Xsize
        self.ySize = Ysize
        self.Pmat = PMatrix
        self.Lmat = lMatrix
        self.calcHologramGrid
        self.calculateIntensity
        self.beamRad = beamRadiusPercent
        self.calcHologramGrid
        self.calculateIntensity


    def __init__(self): # normalizeZeroOne, rowToCol):
        self.normalize = True
        self.rowToCol = 1





