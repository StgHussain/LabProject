from LgBeam import LgBeam
import time
import tkinter as tk

from Utility import Utility
from AddGrating import Addgrating


GRAT = Addgrating()
UTIL = Utility()
p = 1
l = 5
grid = [1920, 1080]
w = 0.12077
t1 = time.time()
<<<<<<< HEAD
gratingType = 'blazed'
gratingAngle = 45
gratingNum = 20
newHolo = LgBeam(p, l, w, grid, gratingType, gratingAngle, gratingNum)
=======
newHolo = LgBeam(0, 10, w, grid)
newHolo2 = LgBeam(1, 1, w, grid)
one = newHolo.returnAns()
two = newHolo2.returnAns()
final = one + two

final = GRAT.addBlazedGrating(final,45, 50, grid)
UTIL.showImg(final)

>>>>>>> 6102d024ada9e9a891638da9d44639e844511cf6
print(time.time() - t1)
