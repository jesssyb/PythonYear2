#Factorial
#Jessica

def ans(n):
    if n > 1:
        return n*ans(n-1)
    else:
        return n*n

def process(n):
    ans = 1
    for x in range(n):
        ans *= (x+1)
        print (ans/(x+1),"*",x+1,"=",ans)
    

def main():
    n = int(input("Enter a whole number: "))
    print ("Factorial of",n,"is:",ans(n),"\n")
    process(n)
main()
