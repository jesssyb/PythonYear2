#Jessica
#CardError

def main():
    return enter()

def enter():
    num = input("Enter a 14 digit card number: ")
    if len(num) == 14:
        return makelist(num)
    else:
        return enter()
    
def makelist(num):
    card = []
    z = 0
    for n in num[:]:
        app = card.append(num[z])
        z += 1
    return step1(card)

def step1(card):
    i = 0
    Sum = []
    while i  < len(card):
        mult = int(card[i]) * 2
        if mult >= 10:
            sub = mult - 9
            app = Sum.append(sub)
        else:
            app = Sum.append(mult)
        i +=2
   
    return step2(card,Sum)

def step2(card,Sum):
    i = 1
    Sum2 = []
    while i  < len(card):
        app = Sum2.append(int(card[i]))
        i +=2

    return step3(Sum,Sum2)

def step3(Sum,Sum2):
    Sum3 = sum(Sum) + sum(Sum2)
    if Sum3 % 10 == 0:
        Sum3 = "valid"
    else:
        Sum3 = "invalid"

    return display(Sum3)

def display(Sum3):
    print ("The card is",Sum3)
        
    
    
        
    
    
        

    
main()
