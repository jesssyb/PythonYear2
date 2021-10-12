#Jessica
#Presidents and Vice Presidents

pres = ["George Washington", "John Adams", "Thomas Jefferson", "James Madison", "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren", "William Henry Harrison", "John Tyler", "James K. Polk","Millard Fillmore"]
vp = ["John Adams", "Thomas Jefferson", "Aaron Burr", "George Clinton", "Elbridge Gerry", "Daniel D. Tompkins", "John C. Calhoun", "Martin Van Buren", "Richard M. Johnson", "John Tyler", "George M. Dallas", "Millard Fillmore"]
p = set(pres)
v = set(vp)

def both():
    b = p.intersection(v)
    b = list(b)
    c = 1
    for x in b:
        print (str(c)+".",x)
        c +=1
    return b
    

def pres():
    pres = list(p)
    pres = p.difference(v)
    c = 1
    for x in pres:
        print (str(c)+".",x)
        c +=1

def vice():
    vp = list(v)
    vp = v.difference(p)
    c =1
    for x in vp:
        print (str(c)+".",x)
        c+=1

def main():
    print ("Both Presidents and Vice Presidents")
    both()
    print ("\nOnly Presidents")
    pres()
    print ("\nOnly Vice Presidents")
    vice()

main()
