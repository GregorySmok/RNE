import turtle
m = 15
turtle.speed(0)
turtle.pu()
for x in range(21):
    for y in range(-21, 21):
        turtle.goto(x*m, y*m)
        turtle.dot()
turtle.goto(7*m, 7*m)
turtle.pd()
for i in range(4):
    turtle.forward(7*m)
    turtle.right(90)
    turtle.forward(7*m)
    turtle.left(90)
    turtle.forward(7*m)
    turtle.right(90)
turtle.done()
