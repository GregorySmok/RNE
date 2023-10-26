import turtle
m = 10
# turtle.speed(0)
turtle.pu()
turtle.goto(51*m, 5*m)
turtle.seth(90)
turtle.pd()
turtle.right(180)
turtle.forward(5*m)
turtle.right(90)
turtle.forward(50*m)
turtle.right(90)
turtle.forward(5*m)
for i in range(5):
    turtle.seth(90)
    turtle.circle(-5*m, 180)
turtle.pu()
for x in range(51):
    for y in range(12):
        turtle.goto(x*m, y*m)
        turtle.dot()
turtle.done()
