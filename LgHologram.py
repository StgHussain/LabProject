import numpy as np
import scipy as scipy
import math

class LGHologram ():

    def __init__(self, sizeX, sizeY, pMatrix, lMatrix, beamRadiusPercent, normalizeZeroOne, rowToCol):
        self.p = 0
        self.l = 1
        self.grid = lMatrix.shape
        self.N = [sizeY, sizeX]
        self.points = self.N/self.grid
        self.range = self.N/min(self.N)
        pMatrix[1:self.grid(1), 1:self.grid(2)] = pMatrix
        BeamPercent[] = []
        BeamPercent[1:self.grid(1), 1:self.grid(2)] = beamRadiusPercent 
        #self.X = np.linspace(-range[1], range[1], points[1])




