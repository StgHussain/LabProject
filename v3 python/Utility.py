import numpy as np
import math
import matplotlib.pyplot as plt

class Utility():

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def showImg(self, img):
        finalMat = [*zip(*img)]
        plt.matshow(finalMat, aspect = 'auto', cmap = plt.get_cmap('gist_gray'))
        plt.show()

    def calculateBeamRad(self, dimPixel, pixelSize, beamRad):
        pixelSize = pixelSize * 0.000001
        beamRad = beamRad * 0.001
        beamRadPercent =  1/((dimPixel*pixelSize)/beamRad)
        return beamRadPercent
