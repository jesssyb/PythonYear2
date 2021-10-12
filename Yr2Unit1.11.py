#Jessica
#Alphabet

def main():
    return enter()

def enter():
    word = input("Enter a word: ")
    word = word.lower()
    return row(word)

def row(word):
    tof = False
    for letter in range(len(word)-2):
        if ord(word[letter]) + 1 == ord(word[letter+1]) and ord(word[letter+1]) + 1 == ord(word[letter+2]):
            tof = True
    

    return display(tof)

def display(tof):
    if tof == True:
        print ("The word has three successive letters")
    else:
        print ("The word doesn't have three successive letters")
    
main()
