from LgBeam import LgBeam 
import time
from numba import jit
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from numba import jit

class testScript():

    def __init__(self):
        testSize = 1
        Lg = LgBeam()
        testSize = 1
        p = 0
        l = 5
        grid = 1024
        w = 0.12077
        self.runTest(p, l, grid, w, testSize, Lg)

    def runTest(self, p, l, grid, w,  testSize, Lg):
        execTimes1 = [0]*testSize
        for m in range(testSize):
            execTimes1[m] = Lg.start(p, l, w, grid)
        self.writeToFile(execTimes1)

    def writeToFile(self, execTimes):
        df = pd.DataFrame(execTimes)
        writer = ExcelWriter('python results v2.xlsx')
        df.to_excel(writer,'Sheet1',index=False)
        writer.save()

