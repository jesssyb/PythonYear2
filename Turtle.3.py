#Jessica
#Flag Part 1

def redStripe(t):
    index = 0
    x = -200
    y = 130
    while y != -130:
        if index == 0:
            y -= 20
            t.up()
            t.fillcolor("red")
            t.begin_fill()
            t.goto(x,y)
            t.down()
            t.goto((x+400),y)
            t.goto((x+400),(y+20))
            t.goto(x,(y+20))
            t.goto(x,y)
            t.up()
            t.end_fill()
            index +=1
        else:
            y -= 20
            t.up()
            t.fillcolor("white")
            t.begin_fill()
            t.goto(x,y)
            t.down()
            t.goto((x+400),y)
            t.goto((x+400),(y+20))
            t.goto(x,(y+20))
            t.goto(x,y)
            t.up()
            t.end_fill()
            index -=1
    return blueCrnr(t)

def blueCrnr(t):
    t.fillcolor("blue")
    t.begin_fill()
    t.goto(-200,130)
    t.down()
    t.goto(-200,-10)
    t.goto(-50,-10)
    t.goto(-50,130)
    t.goto(-200,130)
    t.end_fill()
    

def main():
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(1)
    t.speed(100)
    t.pencolor("black")
    t.up()
    t.goto(-200,130)
    t.down()
    t.goto(200,130)
    t.goto(200,-130)
    t.goto(-200,-130)
    t.goto(-200,130)
    return redStripe(t)

main()
