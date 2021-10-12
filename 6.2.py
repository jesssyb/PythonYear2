#Jessica

import double6

d = double6.double6()
c = 0
for x in range(10000):
    d6 = False
    for y in range(24):
        d.roll()
        if d.sum() == 12:
            d6 = True
    if d6:
        c+=1
    

print ("You rolled",c,"double 6's which is "+str(round(float(c)/10000,2)*100),"percent of the time")

