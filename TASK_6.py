from turtle import *

speed(15)
left(90)
screensize(5000, 5000)
m = 50
down()
for _ in range(2):
    forward(12 * m)
    right(90)
    forward(19 * m)
    right(90)
up()
forward(4 * m)
right(90)
forward(6 * m)
left(90)
down()
for _ in range(2):
    forward(12 * m)
    right(90)
    forward(6 * m)
    right(90)
up()
for x in range(20):
    for y in range(20):
        goto(x * m, y * m)
        dot()
done()
