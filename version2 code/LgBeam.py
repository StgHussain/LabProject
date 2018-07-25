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
        
        Values = self.LaguerreBeam(p,l, 2*RhoSquaredOverWSquare)
        #print(Values)
        #print("values")

        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        n = sizePoints #change this to match grid sizeS
        Result = [[0]*n for x in range(n)] #n value is the size of the result matrix i.e the grid
        for i in range (n):
            for j in range (n):
                imagNum = complex(0,-l*phi[i][j])
                reqVal = Values[i][j]
                Result[i][j] = Clg * (self.SquareRoot2 * np.power(math.sqrt(RhoSquaredOverWSquare[i][j]), abs(l))) * reqVal * np.exp(-RhoSquaredOverWSquare[i][j]) * np.exp(imagNum)
        gratingAngle = 45
        gratNum = 50
        #print('results')
        #print(Result)

        ResultNew = [np.abs(number) for number in Result]
        maxResult = 0
        for i in range(n):
            maxVal = max(ResultNew[i])
            if maxVal > maxResult:
                maxResult = maxVal
            #print(maxVal)
        #print(maxResult)
        ResultNew = ResultNew/maxResult
        #print("result absolute")
        #print(ResultNew)
        Phi = np.angle(Result)
        #print("phi values")
        #print(Phi)
        imaginaryNum = complex(0, 1)
        complexHologram = [[0]*n for x in range(n)]
        for a in range(n):
            for b in range(n):
                complexHologram[a][b] = ResultNew[a][b] * np.exp(imaginaryNum*Phi[a][b])
        #print("complex hologram")
        #print(complexHologram)
        self.addGrating(complexHologram, gratingAngle, gratNum, sizePoints)


    def addGrating(self, inputHologram, gratingAngle, gratingNum, sizes):
        sizePoints = sizes
        #print("add grating")
        XXcords = np.linspace(-self.PI, self.PI, sizePoints)
        YYcords = np.linspace(-self.PI, self.PI, sizePoints)

        #print("input hologram")
        #print(inputHologram)

        #print("xcords")
        #print(XXcords)
        #print("ycords")
        #print(YYcords)
        #print("correct co ords")

        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        theta = (self.PI/180)* gratingAngle
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        #print("plane")
        #print(plane)
        phase = np.angle(inputHologram)
        #print("phase")
        #print(phase)

        phaseHologram = np.mod(phase + gratingNum*plane, 2*self.PI) - self.PI
        #print("phase hologram")
        #print(phaseHologram)
        intensity = np.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        #self.showImg(phaseHologram)

    def showImg(self, img):
        #print("show image")
        finalMat = [*zip(*img)]
        #print(finalMat)
        plt.matshow(finalMat, aspect = 'auto', cmap = plt.get_cmap('gist_gray'))
        plt.show()
    
    def LaguerreBeam(self, p, l, x):
        #self.y = np.array(p + 1, 1)
        #print ("laguerre")
        #Vals = [2]
        Vals = []
        if p == 0:
            Vals = [[1]*5 for __ in range(5)]
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
        #print("poly coeff")
        #print(PolyCoeff)
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

