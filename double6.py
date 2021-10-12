#Jessica
#4/15
import random

class double6:
    def __init__(self, redDie = 1, blueDie = 1):
        self._redDie = 0
        self._blueDie = 0

    def getRed(self):
        return self._redDie

    def getBlue(self):
        return self._blueDie

    def roll(self):
        self._redDie = random.randrange(1,7)
        self._blueDie = random.randrange(1,7)
        return self._redDie, self._blueDie

    def sum(self):
        return self._redDie + self._blueDie

    
