import numpy as np
from numba import cuda, vectorize
import math
import time
from Laguerre import Laguerre
from AddGrating import Addgrating
from Utility import Utility


class LgBeam2():

    def GenerateLGBeam(self, p, l, w, sizePoints):
        
        @vectorize(['double(double, double)', 'float64(float64, float64)'], target = "cuda")
        def matmul(A, B):
            return A * B

        @vectorize(['complex64(float64, complex64)', 'complex64(double, complex128)'], target = 'cuda')
        def matmulComplex(A, B):
            return A * B
        timeStartGPU = time.time()
        n = sizePoints #change this to match grid sizeS
        XXcords = np.linspace(-1, 1, sizePoints[1])
        YYcords = np.linspace(-1/1, 1/1,  sizePoints[0]) #range/something (both need changing)
        Xcords, Ycords = np.meshgrid(XXcords, YYcords)

        [rho, phi] = self.UTIL.cart2pol(Xcords, Ycords)
        #rhoRows = len(rho)
        #rhoCols = len(rho[0])
        #[rho, phi] = self.cart2pol(Xcords, Ycords)

        RhoSquaredOverWSquare = np.zeros((sizePoints[1], sizePoints[0]))
        RhoSquaredOverWSquare = (rho*rho)/(w*w)
        tim1 = time.time()
        Values = self.LAG.LaguerreBeam(p, l, 2*RhoSquaredOverWSquare)
        #print(Values)
        #tim2 = time.time()
        #print("time laguerre")
        #print(tim2-tim1)
       
        ### VARIABLES SETUP #######################################################################
        factP = math.factorial(p)
        factLP = math.factorial(abs(l) + p)
        Clg = math.sqrt((2*factP/ (self.PI * factLP))) / w
        imgNum = np.multiply(phi, complex(0, -l))

        time1 = time.time()
        RhoSqrt = np.zeros((len(RhoSquaredOverWSquare), len(RhoSquaredOverWSquare[0])), dtype=np.double)
        RhoSqrt = np.sqrt(RhoSquaredOverWSquare) * self.SquareRoot2
        RhoSqrt = np.power(RhoSqrt, abs(l))
        mult1 = cuda.device_array((len(RhoSqrt), len(Values[0])))
        mult2 = cuda.device_array((len(RhoSquaredOverWSquare), len(imgNum[0])))
        ################################################################################

        ### CURRENT GPU IMPLEMENTATION #################################################
        d_RhoSqrt = cuda.to_device(RhoSqrt)
        d_Values = cuda.to_device(Values)
        mult1 = matmul(d_RhoSqrt, d_Values)
        RhoSquaredOverWSquare = np.exp(-RhoSquaredOverWSquare)
        imgNum = np.exp(imgNum)
        mult2 = matmulComplex(RhoSquaredOverWSquare, imgNum)

        Res2 = cuda.device_array((mult1.shape[0], mult2.shape[1]))
        Result = np.zeros((Res2.shape[0], Res2.shape[1]), dtype=np.complex64)
        d_Result = cuda.device_array((Res2.shape[0], Res2.shape[1]))
        Res2 = matmulComplex(mult1, mult2)
        d_Result = matmulComplex(Clg, Res2)
        d_Result.copy_to_host(Result)
        #print("Time GPU Implementation")
        ###############################################################################

        ### FIRST-RUN GPU IMPLEMENTATION THAT FED INDIVIDUAL ROWS TO THE GPU ##########
        """for i in range (0, RhoSqrt.shape[1]):
            A = RhoSqrt[:, i]
            B = Values[:, i]
            A = np.ascontiguousarray(A)
            B = np.ascontiguousarray(B)
            mult1 = np.ascontiguousarray(mult1)
            #d_mult1 = numba.cuda.local.array((len(RhoSqrt), len(RhoSqrt[0])), numba.double) 
            mult1[:, i] = matmul(A, B)
            A = np.exp(-RhoSquaredOverWSquare[:, i])
            B = np.exp(imgNum[:, i])
            mult2[:, i] = matmulComplex(A, B)

        Res2 = np.zeros((mult1.shape[0], mult2.shape[1]), dtype=np.complex64)
        Result = np.zeros((Res2.shape[0], Res2.shape[1]), dtype = np.complex64)
        for j in range (0, Res2.shape[1]):
            A = mult1[:, j]
            B = mult2[:, j]
            Res2 = np.ascontiguousarray(Res2)
            A = np.ascontiguousarray(A)
            B = np.ascontiguousarray(B)
            Result = np.ascontiguousarray(Result)
            Res2[:, j] = matmulComplex(A, B)
            C = np.ascontiguousarray(Res2[:, j])
            C = matmulComplex(Clg, C)
            Result[:, j] = C
        print("Time Old GPU Implementation")"""
        ################################################################################

        ### ORIGINAL NumPy implementation running only on CPU ##########################
        """mult1 = np.multiply(RhoSqrt, Values)
        mult2 = np.multiply(np.exp(-RhoSquaredOverWSquare), np.exp(imgNum))
        Res2 = np.multiply(mult1, mult2)
        Res2 = np.multiply(Res2, Clg)
        Result = Res2
        print("Time CPU Implementation")"""
        ################################################################################

        time2 = time.time()
        #print(time2 - time1)

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
        #self.UTIL.showImg(finalHologram)
        #profile.run("driver(GenerateLGBeam, do_plot = True)", sort="time")



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
        #self.GenerateLGBeam(p, l, w, grid)
   
        