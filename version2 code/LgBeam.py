import numpy as np
import scipy as scipy
import math
import matplotlib.pyplot as plt
import time
from matplotlib import cm
from Laguerre import Laguerre 
import threading
from multiprocessing import Pool 

class LgBeam(threading.Thread):

    def GenerateLGBeam(self, p, l, w, sizepoints):
        sizePoints = sizepoints
        XXcords = np.linspace(-1, 1, sizePoints)
        YYcords = np.linspace(-1/1, 1/1,  sizePoints) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)
        #print (Xcords)
        #print (Ycords)
        #print("co ordinates done")

        [rho, phi] = self.cart2pol(Xcords, Ycords)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        #print(RhoSquaredOverWSquare)
        #print("next")
        
        Values = self.LaguerreBeam(p,l, 2*RhoSquaredOverWSquare, sizePoints)
        #print(Values)
        #print("values")

        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        timeResStart = time.time()

        n = sizePoints #change this to match grid sizeS
        t3 = time.time()
        Result = np.zeros((n, n))
        t4 = time.time()
        print("initial time")
        print(t4-t3)

        for i in range (n):
            for j in range (n):
                imagNum = complex(0,-l*phi[i][j])
                reqVal = Values[i][j]
                Result[i][j] = Clg * (self.SquareRoot2 * np.power(math.sqrt(RhoSquaredOverWSquare[i][j]), abs(l))) * reqVal * np.exp(-RhoSquaredOverWSquare[i][j]) * np.exp(imagNum)
        gratingAngle = 45
        gratNum = 50

        timeResEnd = time.time()
        totalRes = timeResEnd - timeResStart 
        print("total loop time")
        print(totalRes)

        ResultNew = [np.abs(number) for number in Result]
        maxResult = np.amax(ResultNew)

        ResultNew = ResultNew/maxResult
        Phi = np.angle(Result)
        imaginaryNum = complex(0, 1)
        complexHologram = np.zeros((1024, 1024))
        t1 = time.time()
        for a in range(n):
            for b in range(n):
                complexHologram[a][b] = ResultNew[a][b] * np.exp(imaginaryNum*Phi[a][b])
        t2 = time.time()
        maxTime = t2 - t1
        print("time to complex value")
        print(maxTime)
        self.addGrating(complexHologram, gratingAngle, gratNum, sizePoints)


    def addGrating(self, inputHologram, gratingAngle, gratingNum, sizes):
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
        self.showImg(phaseHologram)

    def showImg(self, img):
        finalMat = [*zip(*img)]
        plt.matshow(finalMat, aspect = 'auto', cmap = plt.get_cmap('gist_gray'))
        plt.show()
    
    def LaguerreBeam(self, p, l, x, sizeGrid):
        Vals = []
        t1 = time.time()
        if p == 0:
            Vals = [[1]*sizeGrid for __ in range(5)]
            #print (Vals)
        else:
            for m in range (p):
                factM1 = math.factorial(p + 1)
                numerator = (np.power(-1, m)) * factM1
                factPM = math.factorial(p - m)
                factLM = math.factorial(l + m)
                factM2 = math.factorial(m)
                denom = factPM * factLM * factM2
                Vals.append(numerator/denom)
        #polyVal if needed
        PolyCoeff = np.polyval(Vals, x)
        t2 = time.time()
        lag = t2 -t1
        print("laguerre time")
        print(lag)
        return PolyCoeff

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        #print("lg Beam")

    def start(self, P, L, W, grid):
        obj = LgBeam()
        p = P
        l = L
        w = 0.12077
        grids = grid
        t0 = time.time()    
        obj.GenerateLGBeam(p, l, w, grids)
        t1 = time.time()
        totalTime = t1-t0
        return totalTime

