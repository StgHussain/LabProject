import math 
from LgBeam import LgBeam 

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

Lg = LgBeam()
testSize = 100
execTimes = [0]*testSize
p = 1
l = 1
grid = 1024
w = 0.12207


for m in range(testSize):
    execTimes[m] = Lg.start(p, l, w, grid)
    print(m)

#df = pd.DataFrame(execTimes)
#writer = ExcelWriter('python results.xlsx')
#df.to_excel(writer,'Sheet1',index=False)
#writer.save()


print("done")
