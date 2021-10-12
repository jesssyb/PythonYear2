#Jessica
#4/14

class triangle:
    def __init__(self, side = float(input("Enter triangle side: "))):
        self._side = side
    def getSide(self):
        return self._side
    def area(self):
        #1.7321 is approx for sqrt 3
        return round(((self._side*1.7321)/2)*(0.5) * self._side,2)
    def perimeter(self):
        return self._side * 3
    
