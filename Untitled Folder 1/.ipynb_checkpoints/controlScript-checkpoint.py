from Hologram import Hologram
from LgBeam import LgBeam
from Blazed import Blazed
from Utility import Utility

class controlScript():
    
    def showHologram(self):
        displayImg = self.newHolo.returnResult()
        for hologram in displayImg:
            #hologram = self.blaze.addGrating(hologram)
            self.UTIL.showImg(hologram)
            #self.newHolo.clear()
    
    def passBeams(self, Beams):
        self.newHolo.defBeams(Beams)
    
    def passGratings(self, Gratings):
        self.newHolo.defGratings(Gratings)
        
    def runGratedBeams(self):
        self.newHolo.generateHologramGrat()
    
    def runBeams(self):
        self.newHolo.generateHologram()
        
    def clearBeams(self):
        self.newHolo.generateHologram()
    
    def __init__(self):
        self.newHolo = Hologram((1920, 1080))
        self.UTIL = Utility()
        print('new beams')
        print("Input the number of required columns\n input l, p and/or other variables in the following format") 
        print ("pass the matrix via obj.passBeams()")
        print ("pass in the gratings with obj.passfGratings()")
        print ("generate beams with obj.generateHologram()")
        self.blaze = Blazed(0, 0, (1920, 1080))
        