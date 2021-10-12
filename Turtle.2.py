#Jessica
#Star

def star(t):
    t.up()
    t.goto(-150,-150)
    t.down()
    t.goto(0,150)
    t.goto(150,-150)
    t.goto(-150,75)
    t.goto(150,75)
    t.goto(-150,-150)
    t.up()
    return school(t)
    
def school(t):
    t.goto(0,20)
    t.pencolor("black")
    t.write("School",align = "center",font = ("Calibri",20,"bold"))
    t.goto(0,0)
    t.write("Bulldogs",align = "center",font = ("Calibri",20,"bold"))
    return head(t)

#Extra challenge
def head(t):
    t.pencolor("gold")
    t.goto(0,150)
    t.fillcolor("black")
    t.begin_fill()
    t.down()
    t.goto(35,75)
    t.goto(-35,75)
    t.goto(0,150)
    t.end_fill()
    t.up()
    return arm(t)

def arm(t):
    t.goto(-150,75)
    t.down()
    t.begin_fill()
    t.goto(-40,75)
    t.goto(-70,15)
    t.goto(-150,75)
    t.end_fill()
    t.up()
    t.goto(150,75)
    t.down()
    t.begin_fill()
    t.goto(40,75)
    t.goto(70,15)
    t.goto(150,75)
    t.up()
    t.end_fill()
    return leg(t)

def leg(t):
    t.goto(-150,-150)
    t.down()
    t.begin_fill()
    t.goto(-65,15)
    t.goto(0,-40)
    t.goto(-150,-150)
    t.end_fill()
    t.up()
    t.goto(150,-150)
    t.down()
    t.begin_fill()
    t.goto(65,15)
    t.goto(0,-40)
    t.goto(150,-150)
    t.end_fill()
    
def main():
    import turtle
    t = turtle.Turtle()
    t.hideturtle()
    t.pensize(5)
    t.pencolor("gold")
    t.speed(3)
    return star(t)

    

main()
