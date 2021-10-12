#Jessica
#Conversions

op = open("Units.txt",'r')
infile = []
for x in op:
    infile.append(x.rstrip("\n"))
op.close
for x in range(len(infile)):
    infile[x] = infile[x].split(",")

diction = {}
diction = dict(infile)

print ("     Units of Length")
print ("Fathom     Inches     Miles")
print ("Feet     Kilometers   Rods")
print ("Furlongs   Meters     Yards")

units = input("\nUnits to convert from: ").lower()
convert = input("Units to convert to: ").lower()
length = float(input("Length in "+str(units)+": "))

conversionf = length * float(diction[units])
print ("\nLength converted into feet:", conversionf)
conversion = round(conversionf/float(diction[convert]),4)
print ("Converted",convert,"to",conversion)

               
