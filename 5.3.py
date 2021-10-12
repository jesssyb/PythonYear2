#Jessica
#Palindrome

def inpt():
    w = input("Enter a word/phrase: ")
    return w

def punct(w):
    w = w.lower()
    w2 = ""
    for x in w:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            w2 += x
    return w2

def palindrome(r):
    if len(r) == 1:
        return True
    elif r[0] == r[-1]:
        r = r[1:-1]
        return palindrome(r)
    else:
        return False

def output(r,pal):
    if pal:
        print (r.upper(),"is a palindrome")
    else:
        print (r.upper(),"is not a palindrome")

def main():
    w = inpt()
    remove = punct(w)
    pal = palindrome(remove)
    output(remove,pal)
    
    

main()
