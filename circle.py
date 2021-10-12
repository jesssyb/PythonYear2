#Jessica
#4/14

class circle:
    def __init__(self, radius = int(input("Enter the radius: ")), pi = 3.14):
        self._radius = radius
        self._pi = pi

    def getPi(self):
        return self._pi
    def getRadius(self):
        return self._radius
    
    def area(self):
        return self._pi * (self._radius**2)
    def circumference(self):
        return (2*self._radius)*self._pi

    def _str_(self):
        return ("Radius: "+str(self._radius)+"\nPi: "+str(self._pi))
