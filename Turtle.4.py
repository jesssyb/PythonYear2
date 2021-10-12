#Jessica
#Flag Part 2

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
    t.goto(0,-10)
    t.goto(0,130)
    t.goto(-200,130)
    t.end_fill()
    return whiteStars(t)

def whiteStars(t):
    x = -190
    y = 100
    i = 0
    z = 0
    tot = 0
    while tot != 11:
        if z == 0:
            while i != 5:
                t.pencolor("white")
                t.fillcolor("white")
                t.begin_fill()
                t.up()
                t.goto(x,y)
                t.down()
                t.goto(x+5,y+23)
                t.goto(x+10,y)
                t.goto(x-3,y+15)
                t.goto(x+13,y+15)
                t.goto(x,y)
                t.end_fill()
                y -= 25
                i +=1
            x += 17
            y = 90
            i = 0
            z = 1
        else:
            while i != 4:
                t.pencolor("white")
                t.fillcolor("white")
                t.begin_fill()
                t.up()
                t.goto(x,y)
                t.down()
                t.goto(x+5,y+23)
                t.goto(x+10,y)
                t.goto(x-3,y+15)
                t.goto(x+13,y+15)
                t.goto(x,y)
                t.end_fill()
                y -= 25
                i +=1
            y = 100
            i = 0
            z = 0
            x += 17
        tot +=1
        if tot == 11:
            break
        

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
