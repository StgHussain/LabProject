import numpy as np
import cupy as cp
import math
from numba import vectorize
from glumpy import app, gl, glm, gloo


class Addgrating():

    def selectGrating(self, gratingType, gratingVals, hologram, grid):
        if gratingType == "blazed":
            self.addBlazedGrating(hologram, gratingVals[0], gratingVals[1], grid)#change grid from square to deal with different resoultuions
        else:
            print("no grating")


    def addBlazedGrating(self, inputHologram, gratingAngle, gratingNum, sizes):
        sizePoints = sizes
        XXcords = cp.linspace(-self.PI, self.PI, sizePoints[1])
        YYcords = cp.linspace(-self.PI, self.PI, sizePoints[0])

        Xcords, Ycords = cp.meshgrid(XXcords, YYcords)

        theta = (self.PI/180)* gratingAngle
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        phase = cp.angle(inputHologram)
    
        phaseHologram = cp.mod(phase + gratingNum*plane, 2*self.PI) - self.PI
        intensity = cp.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        return phaseHologram

    def __init__(self):
        self.PI= math.pi