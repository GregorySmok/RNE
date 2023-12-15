import turtle as t

m = 15
t.dot()
t.speed(0)
for i in range(2):
    t.forward(9*m)
    t.right(90)
    t.forward(15*m)
    t.right(90)
t.pu()
t.forward(12*m)
t.right(90)
t.pd()
for i in range(2):
    t.forward(6*m)
    t.right(90)
    t.forward(12*m)
    t.right(90)
t.pu()
t.goto(0 ,0)
for x in range(13):
    for y in range(-15, 1):
        t.goto(x*m, y*m)
        t.dot()
t.done()
