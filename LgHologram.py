import numpy as np
import scipy as scipy
import math
from LgBeam import LgBeam

class LGHologram ():

    def calcHologramGrid(self, Xsize, Ysize, PMatrix, rowCol):
        self.N = [Ysize, Xsize]
        self.points = self.N/self.grid
        self.range = self.N/min(self.N)
        PMatrix[1:self.grid(1), 1:self.grid(2)] = PMatrix
        Xcords = np.linspace(-self.range(1), self.range(1), self.points(1))
        Ycords = np.linspace(-self.range(2)/rowCol, range(2)/rowCol, self.points(2))
        self.FinalGrid = np.meshgrid(Xcords, Ycords)
        self.XX = self.FinalGrid [0]
        self.YY = self.FinalGrid [1]

    def calculateIntensity(self, pMat, lMat, beamRad):
        for i in range (1, self.grid(1)):
            for j in range (1, self.grid(2)):
                pMatVal = pMat[i, j]
                lMatVal = lMat[i,j]
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
        


    def __init__(self, sizeX, sizeY, pMatrix, lMatrix, beamRadiusPercent, normalizeZeroOne, rowToCol):
        self.p = 0
        self.l = 1
        self.grid = lMatrix.shape
        self.normalize = True
        self.calcHologramGrid (sizeX, sizeY, pMatrix, rowToCol)
        self.Intensity = np.zeros[self.N]
        self.normalFactor = self.calculateIntensity(pMatrix, lMatrix, beamRadiusPercent)





