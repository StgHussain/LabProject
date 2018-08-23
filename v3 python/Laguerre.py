import time
import numpy as np
from numba import cuda, vectorize, float32
import math

class Laguerre():

        def __init__(self):
            print("laguerre beam")

        def LaguerreBeam(self, p, l, x):

            """@vectorize(['float64(float64, int64)'], target = 'cuda')
            def MatrixPower(Matrix, power):
                i = 0
                for i in range (0, power):
                    Matrix = Matrix * Matrix
            
                return Matrix

            @vectorize(['float64(float64, float64)'], target= 'cuda')
            def PolyVal(Vals, x):
                n = len(x) - 1
                i = 0
                for i in range (0, len(x)):
                    result = MatrixPower(Vals, n - i)
                    Results = Results + result

                return Results"""

            Vals = np.zeros((p+1, 1))
            if p == 0:
                Vals = Vals + 1
            else:
                for m in range (p+1):
                    factM1 = math.factorial(p + l)
                    numerator = (np.power(-1, m)) * factM1
                    factPM = math.factorial(p - m)
                    factLM = math.factorial(l + m)
                    factM2 = math.factorial(m)
                    denom = factPM * factLM * factM2
                    Vals[p - m][0] = (numerator/denom)
            #polyVal if needed
            #Results = np.zeros((len(x), len(x[0])))
            ### GPU Implementation ###
            #PolyCoeff = self.PolyVal(Vals, x, Results) 
            ### END ###
            PolyCoeff = np.polyval(Vals, x)
            #PolyCoeff = PolyVal(Vals, x)
            print(Vals.dtype)
            print(x.dtype)
            return PolyCoeff
        
        @vectorize
        def Add(self, A, B):
            return A + B

        @vectorize
        def Multiply(self, A, B):
            return A * B