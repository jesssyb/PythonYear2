#Jessica
#CrayolaColors

basic1 = ["Black","Blue","Brown","Green","Orange","Red","Purple","Yellow"]
basic2 = ["Red","Red Orange","Orange","Yellow","Green","Yellow Green","Sky Blue","Blue","Purple","Black","Brown","White"]

b1 = set(basic1)
b2 = set(basic2)

print ("Combined Crayola Basic 8 and Crayola Basic 12:")
c = b1.union(b2)
c = list(c)
c.sort()
a = 1
for x in c:
    print (str(a)+".",x)
    a +=1

print ("Common Crayola Colors of Basic 8 and Basic 12")
common = b2.intersection(b1)
common = list(common)
common.sort()
a = 1
for x in common:
    print (str(a)+".",x)
    a+=1

print ("Different Crayola Colors of Basic 8 and Basic 12")
diff = b2.difference(b1)
diff = list(diff)
diff.sort()
a = 1
for x in diff:
    print (str(a)+".",x)
    a+=1





