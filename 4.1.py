#Jessica
#Top hitters

tophits = {"Gehrig":{"atbats":8061,"hits":2721},"Ruth":{"atbats":8399,"hits":2873},"Williams":{"atbats":7706,"hits":2654}}

hitter = list(tophits.keys())

a = []
b = []
for h in hitter:
    avg = round(float(tophits[h]["hits"])/tophits[h]["atbats"],3)
    a.append([h,avg])
    b.append([h,tophits[h]["hits"]])

for x in range(len(a)):
    print (a[x][0] + " " +str(a[x][1]))

hits = []
for x in hitter:
    hits.append(tophits[x]["hits"])
print ("Average number of hits by all three players:",round(float(sum(hits))/3,1))

for x in range(len(hits)):
    if max(hits) == b[x][1]:
        print ("The player with the most hits is:", b[x][0],"with",b[x][1],"hits")
