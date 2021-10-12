#Jessica
#Baseball

tn = input("Enter the team name: ")
gw = float(input("Enter the number of games won: "))
gl = float(input("Enter the number of games lost: "))

ans = round(gw/(gw + gl),3)*100

if ans >= 50:
    print ("The",tn.title(),"have a winning percentage of:",int(ans),"percent")
else:
    print ("The",tn.title(),"have a losing percentage of:",int(ans),"percent")
