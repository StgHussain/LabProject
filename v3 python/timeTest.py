import LgBeam
import time
from LgBeam import LgBeam
from pandas import ExcelWriter, ExcelFile
import pandas as pd

p = 0
l = 5
w = 0.127077
grid = (1920, 1080)
lg = LgBeam(p, 1, w, grid)
x = list()
time1 = time.time()
for i in range(100):
    lg.GenerateLGBeam(p,l,w, grid)
    time2 = time.time()
    x[i] = time2 - time1
df = pd.DataFrame(x)
writer = ExcelWriter('python gpu results.xlsx')
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
