class gratingParams():

    def getGratType(self):
        return self.gratingType
    
    def setGratType(self, gratType):
        self.gratingType = gratType
    
    def getGratNum(self):
        return self.gratingNum
    
    def setGratNum(self, gratNum):
        self.gratingNum = gratNum
        
    def getGratAngle(self):
        return self.gratingAngle
    
    def setGratAngle(self, gratAngle):
        self.gratingAngle = gratAngle

    def __init__(self, gratingType, gratingAngle, gratingNum):
        self.gratingType = gratingType
        self.gratingAngle = gratingAngle
        self.gratingNum = gratingNum