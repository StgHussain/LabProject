from Utility import Utility
from Blazed import Blazed
import numpy as np

class Hologram():
    
    def returnResult(self):
        return self.result
    
    def defBeams(self, matrixBeams):
        self.beamList = matrixBeams
        
    def defGratings(self, gratings):
        self.gratingList = gratings
    
    def generateHologram(self):
        columnNum = 0
        for columnHologram in self.beamList:
            for beams in columnHologram:
                beams.Generate()
                self.tempHologram = self.tempHologram + beams.returnBeam()     
            self.result.append(self.tempHologram)
            self.result[columnNum] = self.ApplySingleGrating(self.result[columnNum], columnNum)
            self.clear()
            columnNum = columnNum + 1
            
    def clear(self):
        self.tempHologram = np.zeros((1920, 1080), dtype = complex)
    
    def generateHologramGrat(self):
        columnNum = 0
        for columnHologram in self.beamList:
            row = 0
            for beams in columnHologram:
                position = (columnNum, row)
                beams.Generate()
                Beam = beams.returnBeam()
                Beam = self.ApplyMultipleGrating(Beam, position) #need to match the grating matrix to the beam that was just generated, eish (looping should work)
                self.tempHologram = self.tempHologram + Beam
                row = row + 1
            self.result.append(self.tempHologram)
            self.clear()
        return self.result 

    def ApplySingleGrating(self, beamResult, position):
        currCol = 0
        print(self.gratingList)
        for sublist in self.gratingList:
            for grating in sublist:
                if currCol == position:
                    print("adding grating")
                    beamResult = grating.addGrating(beamResult)
            currCol = currCol + 1
        return beamResult
    
    def ApplyMultipleGrating(self, beamResult, position):
        print("new")
        print (beamResult)
        columnPos = position[0]   
        rowPos = position[1]
        column = 0
        for sublist in self.gratingList:
            row = 0
            for grating in sublist:
                if column == columnPos:
                    if row == rowPos:
                        beamResult = grating.addGrating(beamResult)
                        print(beamResult)
                row = row + 1
        return beamResult
               
    def __init__(self, gridRes):
        self.gridRes = gridRes
        self.beamList = list()
        self.gratingList = list()
        self.result = list()
        self.UTIL = Utility()
        self.tempHologram = np.zeros((1920, 1080), dtype = complex)
                                      
        