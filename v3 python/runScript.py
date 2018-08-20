from LgBeam import LgBeam
import time
from numba import vectorize, float32
import numpy as np
import tkinter as tk

targetHardware = 'cpu'

@vectorize(['complex64(complex64, complex64)'], target = targetHardware)
def VectorAdd(A, B):
    return A * B

p = 1
l = 5
grid = [1920, 1080]
w = 0.12077
t1 = time.time()
newHolo = LgBeam(p, l, w, grid)

"""size = 10000

arr1 = np.ones(size, dtype = np.complex64)
arr2 = np.ones(size, dtype= np.complex64)
arr3 = np.zeros(size, dtype = np.complex64)

arr3 = VectorAdd(arr1, arr2)
#print(arr3)"""

print(time.time() - t1)
