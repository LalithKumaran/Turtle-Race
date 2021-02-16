import turtle
import random

turtle.screensize(500, 500)
#print(turtle.screensize())
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t1.color('red')
t1.pensize(5)
t1.shape('turtle')
t2.pensize(5)
t2.shape('turtle')
t3.pensize(5)
t3.shape('turtle')
t4.pensize(5)
t4.shape('turtle')
t5.pensize(5)
t5.shape('turtle')
t2.color("blue")
t3.color("yellow")
t4.color('green')
t5.color("black")
t1.penup()
t1.setpos(0, -170)
t1.setheading(90)
t2.penup()
t2.setpos(60, -170)
t2.setheading(90)
t3.penup()
t3.setpos(130, -170)
t3.setheading(90)
t4.penup()
t4.setpos(-60, -170)
t4.setheading(90)
t5.penup()
t5.setpos(-130, -170)
t5.setheading(90)
for i in [t1, t2, t3, t4, t5]:
    i.pendown()
g = []
for i in range(100):
    for i in [t1, t2, t3, t4, t5]:
        if i.position()[1] > 130:
            break
        t1.forward(random.randint(10, 100))

        g.append(("Red", t1.position()))
        t2.forward(random.randint(10, 100))

        g.append(('Blue', t2.position()))
        t3.forward(random.randint(10, 100))

        g.append(("Yellow", t3.position()))
        t4.forward(random.randint(10, 100))

        g.append(("Green", t4.position()))
        t5.forward(random.randint(10, 100))

        g.append(("Black", t5.position()))

h = []
for i in range(-5, 0, 1):
    p = (g[i])
    h.append(p)
q = []
for i, j in h:
    p = i
    d = j[1]
    q.append((p, d))
#print(q)
t = []
for i in reversed(sorted(q, key=lambda x: x[1])):
    t.append(i)
#print(t)
print("The winner is {} turtle".format(t[0][0]))
i = open("pearl.txt", 'w+')
for q in t:

    i.write(f'{q[0]}')
    i.write(f'{q[1]}')
    i.write("\n")







