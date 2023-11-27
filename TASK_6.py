import turtle
m = 20
turtle.speed(0)
turtle.pd()
for i in range(12):
    turtle.right(60)
    turtle.forward(1*m)
    turtle.right(60)
    turtle.forward(1*m)
    turtle.right(270)
turtle.pu()
turtle.goto(-8*m, -5*m)
for x in range(-8, 13):
    for y in range(-5, 13):
        turtle.goto(x*m, y*m)
        turtle.dot()
turtle.done()
