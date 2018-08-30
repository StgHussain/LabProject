from Hologram import Hologram
from LgBeam import LgBeam
from Blazed import Blazed
from Utility import Utility
import time 
from pandas import ExcelWriter, ExcelFile
import pandas as pd
import numpy as np

class controlScript():
    
    def showHologram(self):
        self.display = self.newHolo.returnResult()
        newX = self.grid[0]/self.numCols
        newY = self.grid[1]/self.numCols
        grids = (newX, newY)
        for finalHolo in self.display:
            finalHolo = self.blaze.addGrating(finalHolo, grids)
            self.UTIL.showImg(finalHolo)
        #self.newHolo.clear()         
    
    def passBeams(self, Beams):
        self.newHolo.defBeams(Beams)
    
    def passGratings(self, Gratings):
        self.newHolo.defGratings(Gratings)
        
    def runGratedBeams(self):
        self.newHolo.generateHologramGrat()
    
    def runBeams(self):
        self.clearBeams()
        self.newHolo.generateHologram()
        
    def clearBeams(self):
        self.newHolo.generateHologram()
        
    def defGrid(self, numCols, grid):
        self.numCols = numCols
        self.grid = grid
        self.newHolo.defScreen(grid, numCols)
    
    def __init__(self):
        self.newHolo = Hologram((1920, 1080))
        self.UTIL = Utility()
        print("Input the number of required columns\n input l, p and/or other variables in the following format") 
        print ("pass the matrix via obj.passBeams()")
        print ("pass in the gratings with obj.passfGratings()")
        print ("generate beams with obj.generateHologram()")
        self.blaze = Blazed(0, 0)
        self.display = list()
        