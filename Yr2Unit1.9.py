#Jessica


def main():
    return enter()

def enter():
    word = input("Enter a word or phrase: ")
    return remove(word)

def remove(word):
    word = word.upper()
    word2 = ""
    for letter in word:
        if ord(letter) >= 65 and ord(letter)<=90:
            word2 += letter
    return palindrome(word2)

def palindrome(word2):
    i = 0
    z = 1
    leng = (len(word2)/2)
    leng2 = len(word2)
    pal = True
    while i < leng:
        if word2[i] != word2[leng2-z]:
            pal = False
            return display(word2,pal)
        i +=1
        z +=1
    
    return display(word2,pal)

def display(word2,pal):
    if pal == True:
        print ("The word is a palindrome")
    else:
        print ("The word is not a palindrome")
    
  

main()

