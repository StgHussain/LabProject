import matplotlib.pyplot as plt
from matplotlib import cm

class ShowHologram():

    def showImg(self, img):
        self.FS = 0
        plt.imshow(img, aspect = 'auto', cmap = plt.get_cmap('binary'))

    def __init__(self):
        self.o = 0


