from LgBeam import LgBeam
import time
from Utility import Utility 
from BeamParams import BeamParams
from AddGrating import Addgrating
import numpy as np
from gratingParams import gratingParams


class runScript():

    def mainMenu(self):
        self.clearAndReturn()
        self.gratingType = ""
        self.gratingNum = 0
        self.gratingAngle = 0
        print ("\nChoose from any of the following options\n1.cmd: obj.singleBeam(p, l, bType, gType, gNum, gAngle, grid)")
        print("\n1.cmd: obj.setBeamNum(X, True/False) ---> Use for superposition of different beams")
        #print ("\n3.cmd: obj.excelRead(filename.xls)")
        #print ("\n4.cmd: obj.multiBeam(NumBeams, p, l, bType, gType, gNum, gAngle, grid)")
        print ("\n5.cmd: obj.Help('functionName')\nfunctionNames are the following:\n\tsetBeamNum\n\tsingleBeam\n\texcelRead\n\tmultiBeam")
            
        
    def Help(self, funcHelp):
        if funcHelp == "setBeamNum":
            result = "\nsetBeamNum takes in 2 arguments:\nX = Integer number of beams you want to run\n True/False = if each beam requires their own grating (True) or only require a final grating applied at the end (False)\n Note: creating arrays for these parameters (besides grid) is the way in which multiple beams are optimally generated\n An example of block of declaration of parameters of 3 beams:\np = [0, 1, 1] \nl = [1, 5, 10]\nbeamType = ['lg beam', 'lg beam', 'lg beam'] --> these values need to be in quotations\ngType = ['blazed', 'blazed',  'blazed'] --> these values need to be in double quotations\ngNum = [10, 50, 100]\ngAngle = [0, 45, 90]\ngrid = (1920, 1080)"
            print(result)
            self.mainMenu()
        if funcHelp == "singleBeam":
            result = "\nsingleBeam generates a single beam with parameters: \np (int), \nl (int),\nbType (string of beam name) is the beam, type\n\tTypes implemented: lg beam \ngType (string of grating type) is grating type, \n\tGratings implemented: blazed, \ngNum(int) is grating number, \ngAngle (int) is grating angle, \ngrid is a tuple (x, y) of the screen resolution"
            print(result)
            return
        if funcHelp == "excelRead":
            result = "Provide a string of the filename with the parameter data, follow templateExcel.xls for detailed instructions"
            print(result)
            return
        if funcHelp == "multiBeam":
            result = "Allows you to concatenate up to 3 different holograms next to each other on a single screen\nParameterNote: creating arrays for these parameters (besides grid) is the way in which multiple beams are optimally generated\n An example of block of declaration of parameters of 3 beams:\nNumBeams = 3\np = [0, 1, 1] \nl = [1, 5, 10]\nbeamType = ['lg beam', 'lg beam', 'lg beam'] --> these values need to be in quotations\ngType = ['blazed', 'blazed',  'blazed'] --> these values need to be in double quotations\ngNum = [10, 50, 100]\ngAngle = [0, 45, 90]\ngrid = (1920, 1080)"
            print(result)
            return
        if funcHelp == 'defPLGrat':
            result = "This function reads in all the required parameters for each beam and their respective gratings. These parameters are passed in as arrays with each index representing a beam \nExample declaration block:\np = [0, 1, 1] \nl = [1, 5, 10]\nbeamType = ['lg beam', 'lg beam', 'lg beam'] #--> these values need to be in quotations\ngType = ['blazed', 'blazed',  'blazed'] #--> these values need to be in quotations\ngNum = [10, 50, 100]\ngAngle = [0, 45, 90]\ngrid = (1920, 1080)\nobj.defPLGrat(p, l, beamType, gType, gAngle, gNum, grid)\n"
            print(result)
            return
        if funcHelp == 'defPL':
            result = "This function reads in all the required parameters for each beam. These parameters are passed in as arrays with each index representing a beam \nExample declaration block:\np = [0, 1, 1] \nl = [1, 5, 10]\nbeamType = ['lg beam', 'lg beam', 'lg beam'] #--> these values need to be in quotations\ngrid = (1920, 1080)\n"
            print(result)
            return
        if funcHelp == 'setFinalGrating':
            result = "This function takes in parameters for a single grating function that will be applied to super position of the beams defined in the defPL() function\nExample usage:\n obj.setFinalGratin('blazed', 50, 45, (1920, 1080))\n"
        result = "No such function"
        return
        
          
    def setBeamNum(self, beams, gratingYN):
        self.NumBeams = beams
        self.L = np.zeros(beams)
        self.P = np.zeros(beams)
        self.ArrayType = list()
        if gratingYN:
            self.gratingInd = True
            print("\nPass these arrays as parameters to:\ncmd: obj.defPLGrat(p, l, beamType, gratingType, grating angle, grating number, grid)\nRun following for more information:\ncmd: obj.Help('defPLGrat')")
        else:
            self.gratingInd = False
            print("Pass in parameters for each beam \ncmd: obj.defPL(P, L, beamType, grid) \nRun following for more information, obj.Help('defPL')")
           
        
    def singleBeam(self, p, l, beamType, gratingType, gratingNum, gratingAngle, grid):
        newBeam = BeamParams(beamType, p, l, grid)
        self.grid = grid
        self.BeamList.append(newBeam)
        self.setFinalGrating(gratingType, gratingNum, gratingAngle, grid)

    def defPLGrat(self, p, l, beamType, gratingType, gratingAngle, gratingNum, grid):
        self.grid = grid
        rangeNum = self.NumBeams #- 1
        for i in range (rangeNum):
            print("i value")
            print(i)
            newBeam = BeamParams(beamType[i], p[i], l[i], grid)
            self.BeamList.append(newBeam)
            newGrat = gratingParams(gratingType[i], gratingNum[i], gratingAngle[i])
            self.GratingList.append(newGrat)
        print("All parameters have been succesfully read in, run the following command to produce the holograms:\ncmd: obj.runBeams()")
        
    def defPL(self, p, l, beamType, grid):
        self.grid = grid
        for i in range (self.NumBeams):
            newBeam = BeamParams(beamType[i], p[i], l[i], grid)
            self.BeamList.append(newBeam)
        print("Pass parameters for the final grating\ncmd: obj.setFinalGrating(grating type, grating number, grating angle, grid)")
             
    def printBeams(self):
        print("working")
        for p in self.BeamList:
            print(p.printParams())
            
    def setFinalGrating(self, gratingType, gratingNum, gratingAngle, grid):
        self.gratingType = gratingType
        self.gratingNum = gratingNum
        self.gratingAngle = gratingAngle
        self.grid = grid
        print("Run the experiment \ncmd: obj.runBeams()")
        
    def runBeams(self):
        self.clearAndReturn()
        beams = self.generateBeams()
        for x in beams:
            self.final = self.final + x    
        if not self.gratingInd:
            self.GRAT.selectGrating(self.gratingType, self.gratingAngle, self.gratingNum, self.final, self.grid)
            self.final = self.GRAT.returnGrating()
        self.GRAT.selectGrating("blazed", 0, 0, self.final, self.grid)
        self.final = self.GRAT.returnGrating()
        self.UTIL.showImg(self.final)
        print("Return to main menu \ncmd: obj.mainMenu()\n or rerun experiment \ncmd: obj.runBeams()")
            
    def generateBeams(self):
        result = list()
        counter = 0
        for i in self.BeamList:
            if i.getBeamType() == "lg beam":
                x = LgBeam(i).returnBeam()
            #if i.getBeamType() == "bessel"
            if self.gratingInd:
                gtype = self.GratingList[counter].getGratType()
                gAngle = self.GratingList[counter].getGratAngle()
                gNum = self.GratingList[counter].getGratNum()
                self.GRAT.selectGrating(gtype, gAngle, gNum, x, (1920, 1080))
                x = self.GRAT.returnGrating()
            result.append(x)
            counter = counter + 1
        return result
    
    def clearAndReturn(self):
        self.final = np.zeros((1920, 1080), dtype=complex)  #change this to allow for different resolutions
        self.MultBeam = True
        self.resultConcat = np.zeros((1920, 1080)) #values 
        return
        
        
    def __init__(self):  
        ("Welcome to hologram generation \n ")
        print ("Run the following to generate Holograms\nobj.mainMenu()")
        self.NumBeams = 0
        self.finalGrat = False
        self.BeamList = list()
        self.GratingList = list()
        self.UTIL = Utility()
        self.GRAT = Addgrating()
        self.gratingInd = False
        self.final = np.zeros((1920, 1080), dtype=complex) #change this to allow for different resolutions

