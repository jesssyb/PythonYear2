#Jessica
#11/6/20

import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(100)

#line segment
t.up()
t.goto(20,30)
t.pensize(5)
t.pencolor("black")
t.down()
t.goto(80,90)
t.pencolor("yellow")
t.dot(15)
t.up()
t.goto(20,30)
t.down()
t.pencolor("yellow")
t.dot(15)
t.up()

#Red dot w tangent
t.goto(70,150)
t.pencolor("red")
t.dot(100)
t.goto(0,200)
t.down()
t.pencolor("blue")
t.goto(200,200)
t.up()

#Blue dots
t.pencolor("dark blue")
t.goto(200,50)
t.down()
t.dot(100)
t.pencolor("blue")
t.dot(50)
t.up()

#Purple line
t.goto(-25,-55)
t.pencolor("purple")
t.down()
t.goto(-80,-40)
t.pencolor("violet")
t.dot(20)
t.up()
t.goto(-25,-55)
t.down()
t.dot(20)
t.up()

#Dark green square
t.goto(-160,-160)
t.pencolor("dark green")
t.down()
t.fillcolor("dark green")
t.begin_fill()
t.goto(-60,-160)
t.goto(-60,-60)
t.goto(-160,-60)
t.goto(-160,-160)
t.end_fill()
t.up()

#Red boarder square
t.goto(50,-100)
t.pensize(3)
t.pencolor("red")
t.fillcolor("orange")
t.down()
t.begin_fill()
t.goto(130,-100)
t.goto(130,-20)
t.goto(50,-20)
t.goto(50,-100)
t.end_fill()
t.up()

#Right triangle
t.goto(-100,50)
t.color("magenta")
t.pensize(5)
t.down()
t.goto(-20,50)
t.goto(-100,120)
t.goto(-100,50)

t.up()

#Cyan triangle
t.goto(-150,150)
t.pencolor("cyan")
t.down()
t.goto(-50,150)
t.goto(-100,250)
t.goto(-150,150)
