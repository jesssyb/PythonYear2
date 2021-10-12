#Jessica
#NHL and MLB

def infile():
    infile = ["NHL_Original_6.csv","NHL_Cities_Mascot.csv","MLB_Cities_Mascots.csv"]
    l = []
    for x in infile:
        op = open(x,'r')
        for x in op:
            l.append(x.strip("\n"))
        op.close()
    for x in range(len(l)):
        l[x] = l[x].split(',')
        
    return l

def newTeams(l):
    og = []
    nt = []
    for x in range(len(l)):
        if x <= 5:
            og.append(str(l[x][0])+" "+l[x][1])
        elif x > 5 and x <= 36:
            nt.append(str(l[x][0])+" "+l[x][1])
            
    og = set(og)
    nt = set(nt)
    diff = nt.difference(og)
    diff = list(diff)
    diff.sort()
    print ("Teams not a part of the NHL original 6:\n")
    for x in range(len(diff)):
        print (diff[x])
    
def overlapCity(l):
    mlb = []
    nhl = []
    for x in range(len(l)):
        if x <= 36:
            nhl.append(l[x][0])
        else:
            mlb.append(l[x][0])
    mlb = set(mlb)
    nhl = set(nhl)
    inter = mlb.intersection(nhl)
    inter = list(inter)
    inter.sort()
    print ("\nThe NHL and MLB have teams in these cities:")
    for x in range(len(inter)):
        print (inter[x])

def overlapMascot(l):
    mlb = []
    nhl = []
    for x in range(len(l)):
        if x <= 36:
            nhl.append(l[x][1])
        else:
            mlb.append(l[x][1])
    mlb = set(mlb)
    nhl = set(nhl)
    inter = mlb.intersection(nhl)
    inter = list(inter)
    inter.sort()
    print ("\nThe NHL and MLB have this mascot in common:")
    for x in range(len(inter)):
        print (inter[x])

def count(l):
    mas = []
    for x in range(len(l)):
        mas.append(l[x][1])
    mas = set(mas)
    mas = list(mas)
    mas.sort()
    print ("\nTotal number of non-duplicate mascots: "+str(len(mas)))
    c = 0
    lc = []
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for a in alpha:
        c = 0
        for m in range(len(mas)):
            if a == mas[m][0].upper():
                c +=1
        lc.append(c)
    print ("Letter,Count")
    for i in range(len(alpha)):
        print (alpha[i]," ",lc[i])


def main():
    l = infile()
    newTeams(l)
    overlapCity(l)
    overlapMascot(l)
    count(l)
main()
