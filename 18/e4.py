import random
import turtle as tur
from turtle import Turtle, Screen

colors = ['forestGreen', 'gold', 'hotpink', 'lightgreen', 'lightseagreen', 'magenta4',
          'maroon3', 'mistyrose', 'mediumPurple2', 'orchid4', 'plum4', 'limegreen']

tur.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


t = Turtle()
t.pensize(10)
t.speed('fastest')
directions = [0, 90, 180, 270]  # directions / angles

for _ in range(200):
    # t.pencolor(random.choice(colors))

    t.color(random_color())
    # sets where the turtle should head in angles
    t.setheading(random.choice(directions))
    t.forward(30)

# def left():
#     t.left(90)
#     t.forward(30)


# def right():
#     t.right(90)
#     t.forward(30)


# def straight():
#     t.forward(random.randint(-1, 1) * 30)


# while True:
#     t.pencolor(random.choice(colors))
#     r = random.randint(0, 2)
#     if r == 0:
#         left()
#     elif r == 1:
#         right()
#     else:
#         straight()

s = Screen()
s.exitonclick()
