#Jessica
#Banner

import turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(5)

f = ["S","C","H","O","O","L"]
pc = ["cyan","green","violet","crimson","pink","purple"]
z = True
index = 0
while z == True:
    x = -225
    y = 0
    t.pensize(5)
    t.up()
    for ch in f:
        t.pencolor(pc[index])
        t.goto(x,y)
        t.down()
        t.write(ch,align="center",font = ("Helvetica",50,"bold"))
        x +=60
    index +=1
    if index == 6:
        index = 0
    
    
        

        
