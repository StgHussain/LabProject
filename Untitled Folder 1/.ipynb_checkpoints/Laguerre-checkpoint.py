import time
import numpy as np
import math

class Laguerre():

        def __init__(self):
            lag = 1

        def LaguerreBeam(self, p, l, x):
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
            PolyCoeff = np.polyval(Vals, x)
            return PolyCoeff