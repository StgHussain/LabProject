import time
import numpy as np
import cupy as cp
from numba import cuda
import math

class Laguerre():

        def __init__(self):
            print("laguerre beam")

        def LaguerreBeam(self, p, l, x):
            Vals = cp.zeros((p+1, 1))
            if p == 0:
                Vals = Vals + 1
            else:
                for m in range (p+1):
                    factM1 = math.factorial(p + l)
                    numerator = (cp.power(-1, m)) * factM1
                    factPM = math.factorial(p - m)
                    factLM = math.factorial(l + m)
                    factM2 = math.factorial(m)
                    denom = factPM * factLM * factM2
                    Vals[p - m][0] = (numerator/denom)
            #polyVal if needed
            Results = cp.zeros(len(x), len(x[0]), dtype = float)
            ### GPU Implementation ###
            PolyCoeff = self.PolyVal(Vals, x, Results)
            ### END ###
            #PolyCoeff = cp.polyval(Vals, x)
            return PolyCoeff
        
        @cuda.jit
        def Add(self, A, B):
            return A + B

        @cuda.jit
        def Multiply(self, A, B):
            return A * B

        @cuda.jit
        def MatrixPower(self, Matrix, power):
            i = 0
            for i in range (0, power):
                Matrix = Matrix * Matrix
            
            return Matrix

        @cuda.jit
        def PolyVal(self, Vals, x, Results):
            n = len(x) - 1
            i = 0
            for i in range (0, len(x)):
                result = self.MatrixPower(Vals, n - i)
                Results = Results + result

            return Results