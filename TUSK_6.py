import turtle
turtle.left(90)
m = 30
turtle.speed(0)
for i in range(3):
    turtle.forward(7*m)
    turtle.right(90)
turtle.forward(10*m)
for i in range(3):
    turtle.right(90)
    turtle.forward(6*m)
    
turtle.pu()
turtle.pencolor('white')
for x in range(-16, 16):
    for y in range(-16, 16):
        turtle.goto(x*m, y*m)
        turtle.dot(2)
turtle.done()
