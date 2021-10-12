#Jessica
#Sum

def enter(n):
    yn = 'y'
    while yn.lower() == 'y':
        n.append(int(input("Enter a number: ")))
        yn = input("Do you have a another number to enter? Y or N: ")
    return n

def rsum(n):
    a = 0
    if len(n) == 1:
        return a + n[0]
    else:
        return a + n[0] + rsum(n[1:])

def output(n,s):
    print ("\nThe sum of the numbers",n,"is:",s)
    

def main():
    n = []
    s = 0
    n = enter(n)
    s = rsum(n)
    n.sort()
    output(n,s)
main()
    
