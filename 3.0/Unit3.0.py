#Jessica
#NumberText


def total(n):
    return int(len(n))

def high(n):
    return int(max(n))

def low(n):
    return int(min(n))

def sumof(n):
    return int((sum(n)))

def avg(n):
    return round((sum(n)/7),2)

def display():
    num = open("num.txt","r")
    n = []
    print ("The numbers in the file are:")
    for x in num:
        n.append(float(x.rstrip()))
        print (x,)
    num.close()
    print
    print ("The total number of elements are:",total(n))
    print ("The highest value is:",high(n))
    print ("The lowest value is:",low(n))
    print ("The sum of the values is:",sumof(n))
    print ("The average of the values is:",avg(n))
    


display()
