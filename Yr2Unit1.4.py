#Jessica
#Monogram

def mono(name):
    f = name[0]
    sp = name.find(" ")
    m = name[sp + 1]
    sp2 = name.rfind(" ")
    l = name[sp2+1]
   
    return display(f,m,l)

def display(f,m,l):
    print ("Your monogram is:",f.lower()+m.upper()+l.lower())
    

def enter():
    name = input("Enter your name, (first, middle, last): ")
    return mono(name)

enter()
    
