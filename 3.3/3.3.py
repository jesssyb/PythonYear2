#Jessica
#50 States

def infile():
    op = open("50States.txt",'r')
    l = []
    for x in op:
        l.append(x.strip())
    op.close()

    l2 = []
    for y in range(len(l)):
        split = l[y].split(',')
        app = l2.append(split)
    return l2
        
def enter():
    return input("Enter the name of a state: ").lower()

def state():
    inpt = enter()
    for z in range(len(infile())):
        if infile()[z][0].lower() == inpt:
            print ("The state capital, nickname, and abbreviation:")
            c = 1
            while c != 4:
                if c < 3:
                    print (infile()[z][c]+str(","),)
                elif c == 3:
                    print (infile()[z][c],"\n")

                c+=1
    return same()

def same():
     print ("The states and state capitals that start with the same letter:")
     for a in range(len(infile())):
         if infile()[a][0][0].lower() == infile()[a][1][0].lower():
             print (infile()[a][0]+str(","),infile()[a][1])
     return capital()

def capital():
    print ("\nCapitals of states in alphabetical order:")
    l = []
    for b in range(len(infile())):
        l.append(infile()[b][1])
    l.sort()
    for z in l:
        print (z+str(","),)
        for x in range(len(l)):
            if z == infile()[x][1]:
                print (infile()[x][0])
    return nickname()

def nickname():
    print ("\nNicknames for each states in reverse order:")
    l = []
    for b in range(len(infile())):
        l.append(infile()[b][2])
    l.sort()
    l.reverse()
    for x in range(len(l)):
        print (l[x])
    
state()
