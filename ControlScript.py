import numpy as np
import math
from ShowHologram import ShowHologram
from LgHologram import LgHologram
from AddGrating import AddGrating
from ShowHologram import ShowHologram

sizeGrid = [1024, 1024]
l = [0]
p = [0]
complexAmplitude = True

gratingNumber = 50
gratingAngle = 45
beamRadius = 1
gratingType = 'blazed'

lgHolo = LgHologram()
addHolo = AddGrating()
showHolo = ShowHologram()



returned, matrixOne = lgHolo.generateHologram(sizeGrid[0], sizeGrid[1], p, l, 0.11)
print (matrixOne)
#matrixTwo = addHolo.addgrate(matrixOne, gratingNumber, gratingAngle, complexAmplitude, gratingType)
#print (matrixTwo)
#showHolo.showImg(matrixTwo)
