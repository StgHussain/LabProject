import matplotlib.pyplot as plt
from matplotlib import cm

class ShowHologram():

    def __init__(self, img, fs, map, filename):
        self.FS = 0
        plt.imshow(img, aspect = 'auto', cmap = plt.get_cmap('binary'))


