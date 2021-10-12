import random
import contestants

rps = ["Rock", "Paper", "Scissors"]
c = contestants.RPS()
h = contestants.human()
comp = contestants.computer()
c1 = 0; c2 = 0

c.setName(input("Enter name: "))

def humChoice():
    tof = False
    while tof == False:
        h.setHum(input("Enter rock, paper, or scissors: "))
        if h.getHum().lower() == "paper" or h.getHum().lower() == "rock" or h.getHum().lower() == "scissors":
            tof = True
            return compChoice()
        else:
            return humChoice()

def compChoice():
    comp.setComp(random.choice(rps))

def outcome(c1,c2):
    if h.getHum().lower() == comp.getComp().lower():
        print ("Tie of",h.getHum().lower(),"to",comp.getComp().lower()+str("!"))
        c.setScore(c1+1,c2+1)#c1 += 1; c2 += 1
    elif h.getHum().lower() == "paper" and comp.getComp().lower() == "rock":
        print (c.getName().title(),"drew paper while computer drew rock, human win!")
        c.setScore(c1+1,c2)#c1 += 1
    elif h.getHum().lower() == "paper" and comp.getComp().lower() == "scissors":
        print (c.getName().title(),"drew paper while computer drew scissors, computer win!")
        c.setScore(c1,c2+1)#c2 += 1
    elif h.getHum().lower() == "rock" and comp.getComp().lower() == "paper":
        print (c.getName().title(),"drew rock while computer drew paper, computer win!")
        c.setScore(c1,c2+1)#c2 += 1
    elif h.getHum().lower() == "rock" and comp.getComp().lower() == "scissors":
        print (c.getName().title(),"drew rock while computer drew scissors, human win!")
        c.setScore(c1+1,c2)#c1 += 1
    elif h.getHum().lower() == "scissors" and comp.getComp().lower() == "rock":
        print (c.getName().title(),"drew scissors while computer drew rock, computer win!")
        c.setScore(c1,c2+1)#c2 += 1
    elif h.getHum().lower() == "scissors" and comp.getComp().lower() == "paper":
        print (c.getName().title(),"drew scissors while computer drew paper, human win!")
        c.setScore(c1+1,c2)#c1 += 1
    
    c.getScore()

    again = input("Would you like to go again? (Y or N): ")
    if again.lower() == 'y':
        return main()
    
def main():
    humChoice()
    compChoice()
    outcome(c1,c2)
    

main()
