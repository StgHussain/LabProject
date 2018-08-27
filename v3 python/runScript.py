from LgBeam import LgBeam
import time
import tkinter as tk

p = 1
l = 5
grid = [1920, 1080]
w = 0.12077
t1 = time.time()
gratingType = 'blazed'
gratingAngle = 45
gratingNum = 20
newHolo = LgBeam(p, l, w, grid, gratingType, gratingAngle, gratingNum)
print(time.time() - t1)
