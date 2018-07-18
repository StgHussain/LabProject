import numpy as np
import math
from ShowHologram import ShowHologram
from LgHologram import LgHologram

sizeGrid = [1024, 1024]
l = 0
p = 0
complexAmplitude = True

gratingNumber = 50
gratingAngle = 45
beamRadius = 1

lgHolo = LgHologram()

matrixOne = lgHolo.generateHologram(sizeGrid[0], sizeGrid[1], p, l, 0.11)