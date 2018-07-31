import math 
from LgBeam import LgBeam 

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import threading


Lg = LgBeam()
testSize = 1
execTimes = [0]*testSize
p = 0
l = 5
grid = 1024
w = 0.12077

#test1 = np.array((1000, 1000))
#test2 = np.array((1000, 1000))

#ans = np.multiply(test1, test2)
#print("done")


for m in range(testSize):
    execTimes[m] = Lg.start(p, l, w, grid)

#    print(m)

#df = pd.DataFrame(execTimes)
#writer = ExcelWriter('python results v2.xlsx')
#df.to_excel(writer,'Sheet1',index=False)
#writer.save()


print("done")
