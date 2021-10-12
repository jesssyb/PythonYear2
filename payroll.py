class employee:
    def __init__(self, name = "", hrwk = 1.0, hrwg = 1.0):
        self._name  = name
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

class Hourly(employee):
    def hourlyPay(self, hrwk, hrwg):
        self._hrwk = hrwk
        self._hrwg = hrwg
        return self._hrwg*self._hrwk

class Salary(employee):
    def setSalaryPay(self, wksl):
        self._wksl = wksl
    def getSalaryPay(self):
        return self._wksl
    
