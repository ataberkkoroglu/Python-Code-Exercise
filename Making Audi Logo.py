import turtle

sc=turtle.Turtle()

turtle.title("Circle")
turtle.pencolor("Red")
print(turtle.pos())
turtle.bgcolor("Black")

pen=turtle.shape("turtle")
turtle.pensize(10)
turtle.speed(2)
turtle.setpos(40.00,0.00)
turtle.circle(50,360)
turtle.fillcolor("Yellow")
turtle.shapesize(0.7,0.7)
turtle.setpos(-00.00,00.00)
turtle.pencolor("Yellow")
turtle.circle(50,360)
print(turtle.pos())
turtle.setpos(-40.00,00.00)
turtle.pencolor("Blue")
turtle.circle(50,360)
turtle.setpos(-80.00,00.00)
turtle.pencolor("Purple")
turtle.circle(50,360)
turtle.setpos(-120.00,00.00)
turtle.pencolor("Maroon")
turtle.circle(50,360)
turtle.hideturtle()
turtle.done()