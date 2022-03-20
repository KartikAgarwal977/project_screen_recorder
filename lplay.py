import turtle
def lplay() :
    """ This is the logo of our recorder"""

    t = turtle.Turtle()
    
    t.speed(85)
    turtle.bgcolor("yellow")
    turtle.color("red","red")
    turtle.pensize(5)
    turtle.begin_fill()
    turtle.circle(90)
    turtle.end_fill()
    turtle.setheading(90)
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.forward(180)
    turtle.begin_fill()
    turtle.setheading(-45)
    turtle.color("black")
    turtle.forward(130)
    turtle.setheading(-135)
    turtle.color("black")
    turtle.forward(130)
    turtle.end_fill()
    turtle.bye()

  
