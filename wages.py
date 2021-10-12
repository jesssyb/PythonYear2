class wages:
    def __init__(self, name = "", hrwk = 1.0, hrwg = 1.0):
        self._name = name
        self._hrwk = hrwk
        self._hrwg = hrwg

    def setName(self, name):
        self._name = name

    def setHoursWorked(self, hrwk):
        self._hrwk = hrwk

    def setHourlyWage(self, hrwg):
        self._hrwg = hrwg

    def getName(self):
        return self._name
    def getHoursWorked(self):
        return self._hrwk
    def getHourlyWage(self):
        return self._hrwg

    def pay(self):
        if self._hrwk <= 40:
            pay = self._hrwk * self._hrwg
        else:
            pay = (40 * self._hrwg) + ((self._hrwk - 40) * 1.5 * self._hrwg)
    
        return pay
