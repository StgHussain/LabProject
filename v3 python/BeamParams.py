class BeamParams():

    def setBeamType(self, newBeam):
        self.beamType = newBeam
    
    def getBeamType(self):
        return self.beamType
    
    def setP(self, newP):
        self.p = newP
    
    def getP(self):
        return self.p
        
    def setL(self, newL):
        self.l = newL
    
    def getL(self):
        return self.l
        
    def setGrid(self, newGrid):
        self.grid = newGrid
        
    def getGrid(self):
        return self.grid
        
    def setGratingAngle(self, gratingAngle):
        self.gratingAngle = gratingAngle
        
    def getGratingAngle(self):
        return self.gratingAngle
        
    def setGratingType(self, gratingT):
        self.gratingType = gratingT
        
    def getGratingType(self):
        return self.gratingType
        
    def setGratingNum(self, gratingNum):
        self.gratingNum = gratingNum
        
    def getGratingNum(self):
        return self.gratingNum
    
    def printParams(self):
        print(self.beamType)
        print(self.p) 
        print(self.l) 
        print(self.grid)
        print(self.gratingAngle)
        print(self.gratingNum)
        print(self.gratingType)
        

    def __init__(self, beamType, p, l, grid):
        self.beamType = beamType
        self.p = p
        self.l = l
        self.grid = grid
        