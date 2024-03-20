from turtle import *

tracer(0)
left(90)
screensize(5000, 5000)
k = 60
right(45)
for _ in range(6):
    forward(10 * k)
    right(60)
up()
for x in range(0, 20):
    for y in range(-20, 9):
        goto(x * k, y * k)
        dot(4, 'red')
done()
