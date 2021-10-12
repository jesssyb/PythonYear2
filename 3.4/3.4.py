#Jessica
#Continents

def infile():
    op = open("Continent.txt",'r')
    l = []
    for x in op:
        l.append(x.rstrip())
    op.close()

    l2 = []
    for x in range(len(l)):
        split = l[x].split(',')
        app = l2.append(split)

    for x in range(len(l2)):
        l2[x][2] = eval(l2[x][2])
        l2[x][3] = eval(l2[x][3])
    return l2

def area():
    print ("Countries organized by area in increasing order:")
    l = []
    for x in range(len(infile())):
        l.append(infile()[x][3])
    l.sort()
    for x in l:
        print (x,)
        for z in range(len(l)):
            if x == infile()[z][3]:
                print (infile()[z][0])

    return area3()

def area3():
    print ("\nTop 3 countries with the most area:")
    l = []
    for x in range(len(infile())):
        l.append(infile()[x][3])
    l.sort()
    l.reverse()
    c = 0
    for x in l:
        print (x,)
        for z in range(len(l)):
            if x == infile()[z][3]:
                print (infile()[z][0])
        c+=1
        if c == 3:
            break
    return pop()

def pop():
    print ("\nCountries organized by increasing population:")
    l = []
    for x in range(len(infile())):
        l.append(infile()[x][2])
    l.sort()
    for x in l:
        print (x,)
        for z in range(len(l)):
            if x == infile()[z][2]:
                print (infile()[z][0])

    return pop3()

def pop3():
    print ("\nTop 3 countries with highest population:")
    l = []
    for x in range(len(infile())):
        l.append(infile()[x][2])
    l.sort()
    l.reverse()
    c = 0
    for x in l:
        print (x,)
        for z in range(len(l)):
            if x == infile()[z][2]:
                print (infile()[z][0])
        c +=1
        if c == 3:
            break    
    
area()
