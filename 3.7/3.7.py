#Jessica
#Fuel Economy

def infile():
    infile = open("Fuel+Economy.csv",'r')
    l = []
    for x in infile:
        l.append(x.rstrip("\n"))
    infile.close()

    nl = []
    for x in range(len(l)):
        split = l[x].split(',')
        nl.append(split)
    return nl  

def order():
    l = infile()
    nl = []
    for x in range(len(l)):
        nl.append(str(l[x][4])+' '+str(l[x][2]))
    nl.sort()
    nl.reverse()
    print ("Least fuel efficient cars to most fuel efficient cars \nGals, Model:")
    for x in range(len(l)):
        print (nl[x])

def top3():
    c = []
    m = []
    l = []
    lst = infile()
    for x in range(len(lst)):
        if lst[x][0].lower() == "compact":
            c.append(str(lst[x][0])+" "+str(lst[x][1])+" "+str(lst[x][2])+" "+str(lst[x][4]))            
        elif lst[x][0].lower() == "mid size":
            m.append(str(lst[x][0])+" "+str(lst[x][1])+" "+str(lst[x][2])+" "+str(lst[x][4]))
        elif lst[x][0].lower() == "large":
            l.append(str(lst[x][0])+" "+str(lst[x][1])+" "+str(lst[x][2])+" "+str(lst[x][4]))
    c.sort()
    m.sort()
    l.sort()
    print ("\nTop three fuel efficient cars per size\n")
    print ("Compact cars:")
    for x in range(3):
        print (c[x])
    print ("\nMid-size cars:")
    for x in range(3):
        print (m[x])
    print ("\nLarge cars:")
    for x in range(3):
        print (l[x])

def avg():
    l = infile()
    nl = []

    for x in range(len(l)):
        nl.append(str(l[x][1])+","+str(l[x][3]))
    nl.sort()
    for x in range(len(l)):
        nl[x] = nl[x].split(",")
    cm = []
    a = []
    tot = []
    for x in range(len(nl)):
        if x + 2 < len(nl):
            if nl[x][0] == nl[x+1][0] == nl[x+2][0]:
                cm.append(nl[x][0])
                a.append(round((float(nl[x][1])+float(nl[x+1][1])+float(nl[x+2][1]))/3,2))
    for x in range(len(cm)):
        tot.append(str(a[x])+","+cm[x])
    tot.sort()
    for x in range(len(tot)):
        tot[x] = tot[x].split(',')

    print ("\nCar makers and the avgerage miles per gallon least to greatest:")
    for x in range(len(tot)):
        print (tot[x][1]," ",tot[x][0])
        
    
                         
    
                
    

def main():
    order()
    top3()
    avg()
    
main()
