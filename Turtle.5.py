#Jessica
#Cell Phone
import turtle

def cell(t):
    t.up()
    t.pensize(5)
    t.goto(125,-200)
    t.down()
    t.fillcolor("dark grey")
    t.begin_fill()
    t.goto(-125,-200)
    t.goto(-125,200)
    t.goto(125,200)
    t.goto(125,-200)
    t.end_fill()
    t.up()
    return keys(t)

def keys(t):
    i = 0
    x = -80
    y = 80
    c = 0
    tot = 0
    while tot != 3:
        num = ["1","4","7","*","2","5","8","0","3","6","9","#"]
        t.pencolor("white")
        while i != 4:
            t.goto(x,y)
            t.dot(55)
            t.pencolor("black")
            t.dot(50)
            t.pencolor("white")
            t.goto(x,y-30)
            t.write(num[c],align = "center",font = ("Helvetica",40,"bold"))
            y -=80
            i +=1
            c+=1
        x += 80
        y = 80
        i = 0
        tot +=1  
    return numbox(t)
    

def numbox(t):
    t.pencolor("black")
    t.fillcolor("white")
    t.goto(-100,120)
    t.down()
    t.begin_fill()
    t.goto(-100,170)
    t.goto(100,170)
    t.goto(100,120)
    t.goto(-100,120)
    t.end_fill()

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(100)
    return cell(t)

main()
