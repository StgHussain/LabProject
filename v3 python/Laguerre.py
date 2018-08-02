
class Laguerre():

        def __init__(self):
            print("laguerre beam")

        def LaguerreBeam(self, p, l, x, sizeGrid):
            import numpy as np
            import math
            Vals = np.zeros((p+1, 1))
            if p == 0:
                Vals = Vals + 1
            else:
                for m in range (p):
                    print(m)
                    factM1 = math.factorial(p + 1)
                    numerator = (np.power(-1, m)) * factM1
                    factPM = math.factorial(p - m)
                    factLM = math.factorial(l + m)
                    factM2 = math.factorial(m)
                    denom = factPM * factLM * factM2
                    Vals[p+1-1][0] = (numerator/denom)
            #polyVal if needed
            PolyCoeff = np.polyval(Vals, x)
            return PolyCoeff