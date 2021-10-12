#Jessica
#Conversions

def validentry(m):
    if m < 0:
        print ("Invalid")
    else:
        print ("Enter 1 to convert Gallons to Liters")
        print ("Enter 2 to convert Liters to Gallons")
        con = int(input("Enter selection: "))
        if con == 1:
            print (m,"gallons is",GtoL(m),"liters")
        elif con == 2:
            print (m,"liters is",LtoG(m),"gallons")
    
def GtoL(m):
    return round(m * 3.78541,2)

def LtoG(m):
    return round(m * 0.264172,2)
    
def enter():
    m = float(input("Enter the measurement: "))
    validentry(m)
    
   
enter()
 
