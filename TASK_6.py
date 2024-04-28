from turtle import *

left(90)
tracer(0)
screensize(5000, 5000)
m = 50
for _ in range(5):
    forward(9 * m)
    right(90)
    forward(3 * m)
    right(90)
up()
for x in range(4):
    for y in range(10):
        goto(x * m, y * m)
        dot()
done()