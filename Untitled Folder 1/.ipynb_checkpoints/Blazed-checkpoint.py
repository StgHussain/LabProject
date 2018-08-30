import math
import numpy as np

class Blazed():
    
    def addGrating(self, inputHologram):
        XXcords = np.linspace(-self.PI, self.PI, self.grid[1])
        YYcords = np.linspace(-self.PI, self.PI, self.grid[0])

        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        theta = (self.PI/180)* self.GratAng
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        phase = np.angle(inputHologram)
    
        phaseHologram = np.mod(phase + self.GratNum*plane, 2*self.PI) - self.PI
        intensity = np.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        return phaseHologram
    
    def __init__(self, number, angle, grid):
        self.GratNum = number
        self.GratAng = angle
        self.PI = math.pi
        self.grid = grid