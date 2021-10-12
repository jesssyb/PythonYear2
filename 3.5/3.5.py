#Jessica
#Names

def infile():
    op = open("Names.txt",'r')
    l = []
    for x in op:
        l.append(x.rstrip())
    op.close()

    return l

def inpt():
    name = input("Enter a name: ").lower()
    return name
    

def output():
    name = inpt()
    for x in infile():
        if name != x.lower():
            l = infile()
            app = l.append(name.title())
            l.sort()
        elif name == x.lower():
            print (x.title(),"already exists in the list at number",int(infile().index(x))+1)
            remove = l.remove(name.title())
            break
           
    for x in l:
        print (str(int(l.index(x)+1))+".",x)
   
    

output()
