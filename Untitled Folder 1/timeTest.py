import LgBeam
import time
from LgBeam2 import LgBeam2
from pandas import ExcelWriter, ExcelFile
import pandas as pd

p = 0
l = 5
w = 0.127077
grid = (1920, 1080)
lg = LgBeam2(p, 1, w, grid)
x = list()
for i in range(100):
    time1 = time.time()
    lg.GenerateLGBeam(p,l,w, grid)
    time2 = time.time()
    totalTime = time2 - time1
    x.append(totalTime)
df = pd.DataFrame(x)
writer = ExcelWriter('python gpu results.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
