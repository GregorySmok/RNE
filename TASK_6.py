from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
m = 50
forward(9 * m)
right(90)
for _ in range(2):
    forward(3 * m)
    right(90)
    forward(3 * m)
    right(270)
for _ in range(2):
    forward(3 * m)
    right(90)
forward(9 * m)
up()
for x in range(10):
    for y in range(10):
        goto(x * m, y * m)
        dot()
done()
