class RPS:
    def __init__(self, name = " ", score = 0):
        self.name = name
        self.score = score

    def setName(self, name):
        self._name = name
    def getName(self):
        return self._name

    def setScore(self, humScore, compScore):
        self._humScore = humScore
        self._compScore = compScore
    def getScore(self):
        print (self._humScore,"-",self._compScore)

    
class human(RPS):
    def setHum(self, hum):
        self._hum = hum
    def getHum(self):
        return self._hum
        

class computer(RPS):
    def setComp(self, comp):
        self._comp = comp
    def getComp(self):
        return self._comp
    
        
        



