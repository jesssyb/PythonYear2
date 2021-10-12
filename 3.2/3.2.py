#Jessica
#12days

infile = open("12Days.csv",'r')
d = []
for x in infile:
    d.append(x.rstrip())
infile.close()

def main():
    num = int(input("Enter a number between 1 - 12: "))
    if num > 0 and num < 13:
        print ("The gifts for day",num,"are:\n")
        for z in range(len(d)):
            d[z] = d[z].split(',')

        tot = []
        for a in range(num):
            print (d[a][a-a]," ",d[a][1])
            t = tot.append((float(d[a][2])*float(d[a][a-a])))

        print ("The total cost for day",num,"is:",sum(tot))
        tot1 = []
        b = 1
        for n in range((len(tot)-1)):
            t = tot1.append((tot[n]*(num-b)))
            b +=1
        print ("The total cost for",num,"days is:",sum(tot)+sum(tot1))
    else:
        return main()

main()
