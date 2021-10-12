#Jessica
#Soundex

def main():
    return enter()

def enter():
    word = input("Enter a word to be coded: ")
    word = word.lower()
    return coding(word)

def coding(word):
    code = word[0].upper()
    last = ""
    for strg in word[1:].lower():
        if strg in "bfpv" and last != '1':
            code += '1'
            last = '1'
            
        elif strg in "cgjkqsx" and last != '2':
            code += '2'
            last = '2'
            
        elif strg in "dt" and last != '3':
            code += '3'
            last = '3'
            
        elif strg in "l" and last != '4':
            code += '4'
            last = '4'
            
        elif strg in "mn" and last != '5':
            code += '5'
            last = '5'
            
        elif strg in "r" and last != '6':
            code += '6'
            last = '6'
            
    return fourdigit(code)
        

def fourdigit(code):
    if len(code) > 4:
        code = code[ :4]
    else:
        while len(code) < 4:
            code += "0"
    return display(code)
        
def display(code):
    print ("The code is:",code)
    

main()
