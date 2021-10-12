import payroll
p = payroll.employee()
h = payroll.Hourly()
s = payroll.Salary()

employees = []; totPayroll = []; totHours = []
sal = 0

yn = 'y'
while yn.lower() == 'y':
    p.setName(input("Enter name: "))
    employees.append(p.getName().title())
    selection = input("Enter employee classification (S or H): " )
    if selection.lower() == "s":
        s.setSalaryPay(float(input("Enter weekly salary: ")))
        p.setHoursWorked(float(input("Enter total hours worked: ")))
        sal +=1
        totHours.append(p.getHoursWorked())
        totPayroll.append(s.getSalaryPay())
    else:
        p.setHoursWorked(float(input("Enter total hours worked: ")))
        p.setHourlyWage(float(input("Enter hourly wage: ")))
        totHours.append(p.getHoursWorked())
        #Accounting for overtime
        if p.getHoursWorked() > 40:
            totPayroll.append((h.hourlyPay(40, p.getHourlyWage())) + ((p.getHoursWorked() - 40) * 1.5 * p.getHourlyWage()))
        else:
            totPayroll.append(h.hourlyPay(p.getHoursWorked(), p.getHourlyWage()))

    yn = input("Would you like to continue? (Y or N): ")
    
print

for x in range(len(employees)):
    print (employees[x]+(": $")+str(totPayroll[x]))
print ("Number of employees:",len(employees))
print ("Number of salaried employees:",sal)
print ("Total payroll:",sum(totPayroll))
print ("Average number of hours worked:",(sum(totHours)/len(employees)))

