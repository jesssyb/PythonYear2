#Jessica

def interest(face,intr):
    return intr * face

def a(face, price, mat):
    return (face - price) / mat


def b(face, price):
    return (face + price) / 2
     

def y():
    return round(((interest(face,intr) + a(face, price, mat)) / b(face,price) * 100),2)

def display():
    print ("\nintr =", interest(face,intr))
    print ("a =", a(face,price,mat))
    print ("b =",b(face,price))
    print ("ytm =",(y() / 100))
    print ("\nYield to maturity for this bond is:", str(y())+str("%"))
    

def main():
    return display()

face = float(input("Enter the face value of the bond: "))
intr = float(input("Enter the interest rate of the bond: ")) * 0.01
price = float(input("Enter the current market price of the bond: "))
mat = float(input("Enter the years until maturity for the bond: "))

    

main()
