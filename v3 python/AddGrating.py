import numpy as np
import math

class Addgrating():

    def selectGrating(self, gratingType, gratingVals, hologram, grid):
        if gratingType == "blazed":
            self.addBlazedGrating(hologram, gratingVals[0], gratingVals[1], grid)#change grid from square to deal with different resoultuions
        else:
            print("no grating")


    def addBlazedGrating(self, inputHologram, gratingAngle, gratingNum, sizes):
        sizePoints = sizes
        XXcords = np.linspace(-self.PI, self.PI, sizePoints[1])
        YYcords = np.linspace(-self.PI, self.PI, sizePoints[0])

        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        theta = (self.PI/180)* gratingAngle
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        phase = np.angle(inputHologram)
    
        phaseHologram = np.mod(phase + gratingNum*plane, 2*self.PI) - self.PI
        intensity = np.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        return phaseHologram

    def __init__(self):
        self.PI= math.pi