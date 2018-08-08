import numpy as np 
import matplotlib.pyplot as plt
import matplotlib as mpl

class Utility():

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def showImg(self, img):
        finalMat = [*zip(*img)]
        mpl.rcParams['toolbar'] = 'None'
        plt.matshow(finalMat, aspect = 'auto', cmap = plt.get_cmap('gist_gray'))
        plt.axis('off')
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        plt.show()

    def calculateBeamRad(self, dimPixel, pixelSize, beamRad):
        pixelSize = pixelSize * 0.000001
        beamRad = beamRad * 0.001
        beamRadPercent =  1/((dimPixel*pixelSize)/beamRad)
        return beamRadPercent
