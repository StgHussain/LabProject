import numpy as np
import scipy as scipy
import math

class AddGrating():

    def addgrate(self, inputHologram, gratingNumber, gratingAngle, complexAmplitude, gratingType):
        Pi = math.pi
        sizeHolo = np.shape(inputHologram)
        self.x = np.linspace(-Pi, Pi, 1024)
        self.y = np.linspace(-Pi, Pi, 1024)
        self.Grid = np.meshgrid(self.x, self.y)
        self.theta = Pi/180*gratingAngle
        plane = math.sin(self.theta)*(self.Grid[0]) + math.cos(self.theta)*(self.Grid[1])
        #self.phase = np.angle(inputHologram)
        self.phase = 0

        if gratingType == 'sin':
            self.phaseHologram = math.sin(self.phase+ gratingNumber*plane+Pi)
        else:
            self.phaseHologram = (self.phase + gratingNumber*plane) % 2*Pi
            #self.phaseHologram = math.modf(self.phase + gratingNumber*plane, 2*Pi)-Pi
        self.phaseHologram = (self.phaseHologram - Pi)/ (-Pi -Pi)  

    def __init__(self):
        self.i = 0
           



