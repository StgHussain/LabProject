from Utility import Utility
from Blazed import Blazed
import numpy as np
import math

class Hologram():
    
    def returnResult(self):
        return self.result
    
    def defBeams(self, matrixBeams):
        self.beamList = matrixBeams
        
    def defGratings(self, gratings):
        self.gratingList = gratings
        
    def defScreen(self, grid, columns):
        print("in def grid")
        self.gridRes = grid
        self.numCols = columns
        
    def clear(self):
        self.tempHologram = np.zeros(self.gridRes, dtype = complex)
        self.numCols = 1
        self.multiCols = False
    
    def generateHologram(self):
        columnNum = 0
        self.result = list()
        itera = 0
        newX = math.floor(self.gridRes[0]/self.numCols)
        newY = math.floor(self.gridRes[1]/self.numCols)
        gridNew = (newX, newY)
        self.setTempHolo(gridNew)
        for columnHologram in self.beamList:
            for beams in columnHologram:
                beams.setGrid(gridNew)
                beams.Generate()
                self.tempHologram = self.tempHologram + beams.returnBeam()  
            self.result.append(self.tempHologram)
            self.result[columnNum] = self.ApplySingleGrating(self.result[columnNum], columnNum, gridNew)
            columnNum = columnNum + 1
    
    def generateHologramGrat(self):
        counter = 0
        self.result = list()
        for columnHologram in self.beamList:
            for beams in columnHologram:
                newX = math.floor(grid[0]/self.numCols)
                newY = math.floor(grid[1]/self.numCols)
                gridNew = (newX, newY)
                beams.setGrid(gridNew)
                beams.Generate()
                Beam = beams.returnBeam()
                Beam = self.ApplyMultipleGrating(Beam, counter, gridNew)
                self.tempHologram = self.tempHologram + Beam
                counter = counter + 1
            self.result.append(self.tempHologram)
            self.clear() 
        self.joinHolograms()
            
    
    def Cols(self, numCols, multiCols):
        self.numCols = numCols
        self.multiCols = multiCols

    def ApplySingleGrating(self, beamResult, position, newGrid):
        currCol = 0
        for sublist in self.gratingList:
            for grating in sublist:
                if currCol == position:
                    grating.setGrid(newGrid)
                    beamResult = grating.addGrating(beamResult, newGrid)
            currCol = currCol + 1
        return beamResult
    
    def ApplyMultipleGrating(self, beamResult, position, newGrid):
        count = 0
        for sublist in self.gratingList:
            for grating in sublist:
                if count == position:
                    grating.setGrid(newGrid)
                    beamResult = grating.addGrating(beamResult)
                count = count + 1
        return beamResult
    
    def setTempHolo(self, newGrid):
        self.gridRes = newGrid
        self.tempHologram = np.zeros((newGrid), dtype = complex)

               
    def __init__(self, gridRes):
        self.gridRes = gridRes
        self.beamList = list()
        self.gratingList = list()
        self.result = list()
        self.UTIL = Utility()
        self.tempHologram = np.zeros((self.gridRes), dtype = complex)
        self.numCols = 1
        self.multiCols = False
                                      
        