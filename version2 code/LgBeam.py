import numpy as np
import scipy as scipy
import math
import matplotlib.pyplot as plt
import time
from matplotlib import cm
from Laguerre import Laguerre 


class LgBeam():

    def GenerateLGBeam(self, p, l, w, sizepoints):
        sizePoints = sizepoints
        n = sizePoints #change this to match grid sizeS
        XXcords = np.linspace(-1, 1, sizePoints)
        YYcords = np.linspace(-1/1, 1/1,  sizePoints) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((n, n))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)

        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        Result = np.zeros((n, n), dtype=complex)
        imgNum = np.multiply(phi, complex(0, -l))

        time1 = time.time()
       #Result calculation 
        RhoSqrt = np.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = np.power(RhoSqrt, abs(l))
        mult1 = np.multiply(RhoSqrt, Values)
        mult2 = np.multiply(np.exp(-RhoSquaredOverWSquare), np.exp(imgNum))
        Res2 = np.multiply(mult1, mult2)
        Res2 = np.multiply(Res2, Clg)
        Result = Res2
        #Results calculated 
        time2 = time.time()
        print("time for results")
        print(time2-time1)

        gratingAngle = 45
        gratNum = 50

        ResultNew = [np.abs(number) for number in Result]
        maxResult = np.amax(ResultNew)
        ResultNew = ResultNew/maxResult

        time3 = time.time()
        imaginaryNum = complex(0, 1)
        Phi = np.angle(Result)
        Phi = np.multiply(Phi, imaginaryNum)
        Phi = np.exp(Phi)
        complexHologram = np.zeros((n, n), dtype=complex)
        complexHologram = np.multiply(ResultNew, Phi)
        time4 = time.time()
        print("complex hologram time")
        print(time4 - time3)
        #for a in range(n):
        #    for b in range(n):
        #        complexHologram[a][b] = ResultNew[a][b] * np.exp(imaginaryNum*Phi[a][b])
        #print("complex 2")
        #print(complexHologram)
        self.addGrating(complexHologram, gratingAngle, gratNum, sizePoints)


    def addGrating(self, inputHologram, gratingAngle, gratingNum, sizes):
        timeS = time.time()
        sizePoints = sizes
        XXcords = np.linspace(-self.PI, self.PI, sizePoints)
        YYcords = np.linspace(-self.PI, self.PI, sizePoints)

        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        theta = (self.PI/180)* gratingAngle
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        phase = np.angle(inputHologram)
    
        phaseHologram = np.mod(phase + gratingNum*plane, 2*self.PI) - self.PI
        intensity = np.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        timeE = time.time()
        print("grating time")
        print(timeE - timeS)
        self.showImg(phaseHologram)

    def showImg(self, img):
        finalMat = [*zip(*img)]
        plt.matshow(finalMat, aspect = 'auto', cmap = plt.get_cmap('gist_gray'))
        #plt.show()
    
    def LaguerreBeam(self, p, l, x, sizeGrid):
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

    def cart2pol(self, x, y):
        time1 = time.time()
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        time2 = time.time()
        print("time cart to polar")
        print(time2 - time1)
        return(r, Angle)

    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        

    def start(self, P, L, W, grid):
        obj = LgBeam()
        p = P
        l = L
        w = W
        grids = grid
        t0 = time.time()    
        obj.GenerateLGBeam(p, l, w, grids)
        t1 = time.time()
        totalTime = t1-t0
        print("total time:")
        print(totalTime)
        return totalTime

