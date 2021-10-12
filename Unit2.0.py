Concorde2020 = ["School1","School2","School3","School4","School5"]
Concorde2010 = "School1","School2","School3","Shool4","School5","School6"

c2020 = set(Concorde2020)
c2010 = set(Concorde2010)

c = c2010.union(c2020)

print (c)

same = c2020.intersection(c2010)

print (same)

diff = c2020.difference(c2010)

print (diff)
