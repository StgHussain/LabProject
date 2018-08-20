import numpy as np
from numba import cuda
import math
import time
from Laguerre import Laguerre
from AddGrating import Addgrating
from Utility import Utility


class LgBeam():

    @cuda.jit
    def GPUCalculation(self, imgNum, rhoRows, rhoCols, rho, phi, p, l, w, LGBeam, Result):
        i = 0
        j = 0
        for i in range (0, rhoRows):
            for j in range (0, rhoCols):
                Clg = math.sqrt((2 * math.factorial(p[i, j])) / math.pi * math.factorial(abs(l[i, j] + p[i, j]))) / w
                EValue = Clg * math.pow((math.sqrt(2) * math.sqrt(rho[i, j])), abs(l[i, j])) * LGBeam[i,j] * math.exp(-rho[i, j] * math.exp(imgNum * l[i,j] * phi[i,j]))
                Result[i, j] = EValue
        return Result

    @cuda.jit('void(complex[:, :], complex[:, :], complex[:, :])')
    def matmul(A, B, C):
        i, j = cuda.grid(2)
        if i >= A.shape[0]:
            return
        if i < C.shape[0] and j < C.shape[1]:
            tmp = 0
            for k in range(A.shape[1]):
                tmp += A[i, k] * B[k, j]
            C[i, j] = tmp

    @cuda.jit
    def GPUFactorial(self, x):
        result = 1
        while x > 0:
            result = result * x
        return result
    
    def GenerateLGBeam(self, p, l, w, sizePoints):
        n = sizePoints #change this to match grid sizeS
        XXcords = np.linspace(-1, 1, sizePoints[1])
        YYcords = np.linspace(-1/1, 1/1,  sizePoints[0]) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)
        rhoRows = len(rho)
        rhoCols = len(rho[0])
        #[rho, phi] = self.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((sizePoints[1], sizePoints[0]))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        tim1 = time.time()
        Values = self.LAG.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare)
        tim2 = time.time()
        print("time laguerre")
        print(tim2-tim1)

        Result = np.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        imgNum = np.multiply(phi, complex(0, -l))

        #Values = self.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare, sizePoints)
        ### GPU Calculation Call ###
        #Result = self.GPUCalculation(imgNum, rhoRows, rhoCols, rho, phi, p, l, w, Values, Result)

        ### Previous CuPy/Numpy Calculation ###
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w

        imgNum = np.multiply(phi, complex(0, -l))

        time1 = time.time()
      
        RhoSqrt = np.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = np.power(RhoSqrt, abs(l))
        mult1 = np.zeros((len(RhoSqrt), len(Values[0])))
        #A_gpu = cuda.to_device(RhoSqrt)
        #B_gpu = cuda.to_device(Values)
        #C_gpu = cuda.device_array((len(RhoSqrt), len(Values[0])), dtype = complex)
        threadsperblock = 256
        blockspergrid = (len(RhoSqrt) * len(Values[0]) + (threadsperblock -1)) // threadsperblock
        matmul[threadsperblock, blockspergrid](RhoSqrt, Values, mult1)
        mult2 = np.multiply(np.exp(-RhoSquaredOverWSquare), np.exp(imgNum))
        Res2 = np.multiply(mult1, mult2)
        Res2 = np.multiply(Res2, Clg)
        Result = Res2
        
        time2 = time.time()
        print("time numpy")
        print(time2 - time1)
        ### End of old implementation ###

        ResultNew = [np.abs(number) for number in Result]
        maxResult = np.amax(ResultNew)
        ResultNew = ResultNew/maxResult

        imaginaryNum = complex(0, 1)
        Phi = np.angle(Result)
        Phi = np.multiply(Phi, imaginaryNum)
        Phi = np.exp(Phi)
        complexHologram = np.zeros((sizePoints[0], sizePoints[1]), dtype=complex)
        complexHologram = np.multiply(ResultNew, Phi) 
        #replace these with values specified by the user
        gratingAngle = 45
        gratingNum = 50
        ########################################################
        finalHologram = self.GRAT.addBlazedGrating(complexHologram, gratingAngle, gratingNum, sizePoints)
        #finalHologram = self.GRAT.selectGrating(self.gratingType, self,gratingVal, complexHologram, self.Grid)
        #return finalHologram
        self.UTIL.showImg(finalHologram)


    def __init__(self, p, l, w, grid):
        self.SquareRoot2 = math.sqrt(2)
        self.PI= math.pi
        #when this beam type is called all the values and parameters will be set in this function
        #self.gratingType = 
        #self.gratingVal[0] = gratingAngle
        #self.gratingVal[1] = gratingNum
        #self.Grid = gridXY 


        self.LAG = Laguerre()
        self.UTIL = Utility()
        self.GRAT = Addgrating()
        #first parameter is dimension y of grid, 8 not sure, 1 defined by laser used
        #w = self.UTIL.calculateBeamRad(1024, 8, 1)
        #need changes to calculate Beam Radius function 
        w = 0.12077
        self.GenerateLGBeam(p, l, w, grid)
        