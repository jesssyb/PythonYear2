#Jessica
#4/27

class fraction:
    def __init__(self, numerator = 1, denominator = 1, decimal = 0.1):
        print ("Enter 1 - Reduce fraction\nEnter 2 - Convert decimal to fraction\nEnter 3 - Quit")
        self._numerator = numerator
        self._denominator = denominator
        self._decimal = decimal
          
    def setNumerator(self,numerator):
        self._numerator = numerator
    
    def setDenominator(self, denominator):
        self._denominator = denominator
        
    def setDecimal(self, decimal):
        self._decimal = decimal

    def getNumerator(self):
        return self._numerator
    def getDenominator(self):
        return self._denominator
    def getDecimal(self):
        return self._decimal
        
    def reduceFraction(self):
        gcd = 0
        for x in range(1,self._denominator+1):
            if self._numerator % x == 0 and self._denominator % x == 0:
                gcd = x
        print ("\nReduced fraction:",str(self._numerator / gcd)+("/")+ str(self._denominator / gcd))

    def convert(self):
        c = 1
        while self._decimal*c > int(self._decimal*c):
            c *=10
        self._numerator = (int(self._decimal*c))
        self._denominator = (int(c))
        return self.reduceFraction()
