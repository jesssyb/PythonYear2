#Jessica
#Do you have a dog

ans = input("Do you have a dog? Y or N: ")

if ans.lower() == "y":
    name = input("What is your dog's name?: ")
    res = input("Is it a rescue? Y or N: ")
    if res.lower() == "y":
        print ("Enjoy",name.title(),"your rescue dog!")
    else:
        breed = input("What breed is your dog?: ")
        print ("Enjoy",name.title(),"your",breed+str("!"))
else:
    print ("Don't shop, adopt. Consider looking into local shelters.")
