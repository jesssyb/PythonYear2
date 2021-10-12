
#Initialize
d = {2:3,4:5,6:7,8:9,10:11}
print ("Number of items:",len(d))

#key is like index
print ("The value stored at key 2 is:",d[2])

print ("Dictionary:",d)

d = {20:30,2:3,4:5,6:7,8:9,10:11}

print ("New dictionary:",d)

if 10 in d:
    print ("The key 10 is in the dictionary")
else:
    print ("The key 10 is not in the dictionary")

k = 11
if k in d:
    print ("The key " + str(k)+"is in the dictionary")
else:
    print ("The key "+str(k)+"is not in the dictionary")
#k is not in the dictionary bc its a value

d[20] = 25
print ("The dictionary is:",d)

#can add to dictionary
d[22] = 27
print ("Dictionary:",d)

d["24"] = "29"
print ("Dictionary:",d)


d[3.14] = "pi"
print ("Dictionary:",d)

listd = ["f",25]
d["list"] = listd
print ("Dictionary:",d)

print ("The value stored at key list is", d["list"])

for l in d["list"]:
    print (l)

#d.get is like .find for string and .index for list
print ("The value at key is:",d.get("24","The key doesnt exist"))
print ("The value at key is:",d.get(100,"This key doesnt exist"))

key = list(d.keys())
val = list(d.values())
item = list(d.items())

print ("The list of keys is",key)
print ("The list of values is:",val)
print ("The list of items is:",item)

dictn = list(d)
tup = tuple(d)
st = set(d)

print ("The list of the dict is:",dictn)
print ("the tuple of the dict is:",tup)
print ("the set of the dict is:",st)

c = {}
c = dict(d)
print ("\n",c)
del c['24']
print ("\n",c)
c.clear()
print ("\n",c,"\n")

c.update(d)
print (c,"\n")

print ("Highest value in dictionary:", max(d))
print ("Lowest value in dictionary:",min(d))












