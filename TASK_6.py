from turtle import *

left(90)
screensize(5000, 5000)
m = 50
speed(0.1)
dot()
right(135)
for _ in range(7):
    forward(7 * m)
    right(45)
    forward(8 * m)
    right(135)
up()
for x in range(6):
    for y in range(-13, 1):
        goto(x * m, y * m)
        dot()
done()
