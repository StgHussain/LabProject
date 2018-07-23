import numpy as np
import scipy as scipy
import math
import matplotlib.pyplot as plt
from matplotlib import cm
from Laguerre import Laguerre 

class LgBeam():

    def GenerateLGBeam(self, p, l, w):
        
        XXcords = np.linspace(-1, 1, 5)
        YYcords = np.linspace(-1/1, 1/1, 5) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)
        print (Xcords)
        print (Ycords)
        print("co ordinates done")

        [rho, phi] = self.cart2pol(Xcords, Ycords)
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        print(RhoSquaredOverWSquare)
        print("next")
        
        Values = self.LaguerreBeam(p,l, 2*RhoSquaredOverWSquare)
        print(Values)
        print("values")


        Pi = math.pi
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (Pi * factLP))) / w
        Result = []
        for i in range (5):
            for j in range (5):
                imagNum = complex(0,-l*phi[i][j])
                reqVal = Values[i][j]
                Result[i][j] = Clg * (self.SquareRoot2 * np.power(math.sqrt(RhoSquaredOverWSquare[i][j]), abs(l))) * reqVal * np.exp(-RhoSquaredOverWSquare[i][j]) * np.exp(imagNum)
        gratingAngle = 45
        gratNum = 50

        self.addGrating(Result, gratingAngle, gratNum)


    def addGrating(self, inputHologram, gratingAngle, gratingNum):
        print("add grating")
        Xcords = np.linspace(-1, 1, 5)
        Ycords = np.linspace(-1, 1, 5)

        theta = (self.PI/180)* gratingAngle
        plane = math.sin(theta)*Xcords + math.cos(theta)*Ycords
        phase = np.angle(inputHologram)

        phaseHologram = np.mod(phase + gratingNum*plane, 2*self.PI) - self.PI
        intensity = np.abs(inputHologram)

        phaseHologram = phaseHologram * intensity
        phaseHologram = (phaseHologram - self.PI)/(-2*self.PI)
        self.showImg(phaseHologram)

    def showImg(self, img):
        print("show image")
        sizeIm = len(img)
        print(sizeIm)
        plt.imshow(img, aspect = 'auto', cmap = plt.get_cmap('binary'))
    
    def LaguerreBeam(self, p, l, x):
        #self.y = np.array(p + 1, 1)
        print ("laguerre")
        #Vals = [2]
        Vals = []
        if p == 0:
            Vals = [[1]*5 for __ in range(5)]
            print (Vals)
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
        print("poly coeff")
        print(PolyCoeff)
        return PolyCoeff

    def cart2pol(self, x, y):
        r = np.sqrt(x**2 + y**2)
        Angle = np.arctan2(y, x)
        return(r, Angle)

    def __init__(self):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        print("lg Beam")

obj = LgBeam()
p = 0
l = 1
w = 0.12207
obj.GenerateLGBeam(p, l, w)


