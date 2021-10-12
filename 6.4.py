import wages
w = wages.wages()

def enter():
    w.setName(input("Enter employee name: "))
    w.setHoursWorked(float(input("Enter hours worked: ")))
    w.setHourlyWage(float(input("Enter hourly wage: ")))

def output():
    print ("\n",w.getName().title(),"worked", int(w.getHoursWorked()),"hours this week")
    print (w.getName().title(),"makes an hourly wage of $"+str(w.getHourlyWage()))
    print (w.getName().title(),"earned $"+str(w.pay()))

def main():
    enter()
    output()

main()
