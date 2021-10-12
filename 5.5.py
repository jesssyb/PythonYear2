#Jessica
#Alphabet


def alphabet(w,x):
    alpha = False
    if x == 0:
        if ord(w[x][0]) < ord(w[x+1][0]):
            alpha = True
        else:
            alpha = False
    if x > 0:
        if ord(w[x][0]) > ord(w[x-1][0]):
            alpha = True
            return alphabet(w,x-1)
        else:
            alpha = False
            
    return alpha
            
def output(tof):
    if tof == True:
        print ("The list is in alphabetical order")
    else:
        print ("The list is not in alphabetical order")
    
def main():
    w = ["apple","banana","carrot","elephant","donut"]
    x = len(w)-1
    tof = alphabet(w,x)
    output(tof)
    

main()
