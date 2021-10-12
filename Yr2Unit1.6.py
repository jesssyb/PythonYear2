#Jessica

def enter():
    year = int(input("Enter the starting year: "))
    pop = int(input("Enter the population of the year: "))
    return calc(pop,year)


def calc(pop,year):
    c = 0
    while pop <= 8000000000:
        pop += (pop * 0.011)
        c +=1
    year = year + c
    pop = round(pop)
    return display(pop,c,year)
        

def display(pop,c,year):
    print ("The population has increased in",c,"years to",year,"to", int(pop),"people")

def main():
    return enter()

main()
