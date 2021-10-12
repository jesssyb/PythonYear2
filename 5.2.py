#Jessica
#GCD

def enter():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num1 <= 0 or num2 <=0 or int(num1) != num1 or int(num2) != num2:
        enter()
    else:
        return num1,num2
        
def GCD(n2,n):
    print (n)
    print (n2)
    if n == 0:
        return n2
    else:
        return GCD(n,n2%n)

def main():
    n,n2 = enter()
    print ("GCD =",GCD(n2,n))

main()
