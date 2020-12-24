import turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


turtle.colormode(255)
t = turtle.Turtle()
t.speed('fastest')


def draw_spirograph(size):
    for x in range(int(360 / size)):
        t.circle(100)
        t.color(random_color())
        heading = t.heading()
        t.setheading(heading + size)


draw_spirograph(2)

s = turtle.Screen()
s.exitonclick()
