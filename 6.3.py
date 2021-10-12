import fraction
f = fraction.fraction()

def main():
    inpt = int(input("\nEnter selection: "))
    if inpt == 1:
        f.setNumerator(int(input("Enter a numerator: "))), f.setDenominator(int(input("Enter a denominator: ")))
        f.reduceFraction()
    elif inpt == 2:
        f.setDecimal(float(input("Enter a decimal: ")))
        f.convert()
    
    elif inpt == 3:
        print ("\nGoodbye")
    else:
        print ("\nInvalid")
        return main()
    
main()
