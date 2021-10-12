#Jessica
#Gettysburg

address = open("Gettysburg.txt",'r')
add = []
for x in address:
    add.append(x)
address.close()

add2 = ""
for y in str(add):
    if 97 <= ord(y.lower()) <= 172 or 32 == ord(y.lower()) or 44 == ord(y.lower()):
        add2 += y
print (add2)

add3 = []
add3 = add2.split()
tot = 0
del add3[-1] #Removing random 'n'
print ("The first 89 characters:")
for z in add3:
    print (str(z)+"",)
    tot += len(z)+1 #The one is accounting for spaces
    if tot >= 89:
        break
    
print    
print ("\nThe address contains:",len(add3),"words\n")

add4 = []
for a in add3:
    if ord(a[-1]) != 44: #Takes out the commas
        app = add4.append(a.lower())
    

d = set(add4)    
diff = d.intersection(d)
print ("The address contains",len(diff),"different words")


