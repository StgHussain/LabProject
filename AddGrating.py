import numpy as np
import scipy as scipy
import math

class AddGrating():


    def __init__(self, inputHologram, gratingNumber, gratingAngle, complexAmplitude, gratingType, complexAmplitudeType):
        Pi = math.pi
        sizeHolo = np.shape(inputHologram)
        self.x = np.linspace(-Pi, Pi, sizeHolo[0])
        self.y = np.linspace(-Pi, Pi, sizeHolo[1])
        self.Grid = np.meshgrid(self.x, self.y)
        self.theta = Pi/180*gratingAngle
        plane = math.sin(self.theta)*(self.Grid[1]) + math.cos(self.theta)*(self.Grid[2])
        self.phase = np.angle(inputHologram)

        if gratingType == 'sin':
            self.phaseHologram = math.sin(self.phase+ gratingNumber*plane+Pi)
        else:
            self.phaseHologram = math.modf(self.phase + gratingNumber*plane, 2*Pi)-Pi
        self.phaseHologram = (self.phaseHologram - Pi)/ (-Pi -Pi)        



