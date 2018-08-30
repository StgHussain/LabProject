from controlScript import controlScript
import numpy as np
from LgBeam import LgBeam
from Blazed import Blazed

obj = controlScript()
grid = (1920, 1080)
beam = [[LgBeam(0, 1, 1, grid)]]
grat = [[Blazed(10, 45, grid)]]
obj.passBeams(beam)
obj.passGratings(grat)
obj.runBeams()


