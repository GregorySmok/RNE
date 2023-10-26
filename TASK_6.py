import turtle
m = 15
turtle.speed(0)
turtle.pu()
for x in range(-5, 17):
    for y in range(-6, 21):
        turtle.goto(x*m, y*m)
        turtle.dot()
turtle.goto(7*m, 7*m)
turtle.pd()
for i in range(2):
    turtle.forward(3*m)
    turtle.left(90)
    turtle.backward(10*m)
    turtle.left(90)
turtle.pu()
turtle.backward(10*m)
turtle.right(90)
turtle.forward(8*m)
turtle.left(90)
turtle.pd()
for i in range(2):
    turtle.forward(16*m)
    turtle.right(90)
    turtle.forward(8*m)
    turtle.right(90)
turtle.done()
