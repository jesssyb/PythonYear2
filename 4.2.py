#Jessica
#NATO

alpha = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}

name = input("Enter your name: ")
l = ""

for x in name:
    if ord(x) == 32:
        pass
    else:
        l += x
        
for x in l:
    for y in range(len(alpha)):
        if x.upper() in alpha:
            print (alpha[x.upper()])
        break
