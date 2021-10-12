#Jessica
#Prime numbers

def calc(n):
    if n == 1:
        return []
    for x in range(2,n+1):
        if n % x == 0:
            return [x] + calc(n/x)
    
    
def main():
    n = int(input("Enter a whole number: "))
    print ("List of prime factors of",n,"=",calc(n))
    
main()
