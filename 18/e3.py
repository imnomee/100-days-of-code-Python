from random import randint, choice
from turtle import Turtle, Screen
t = Turtle()
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'coral',
          'brown', 'chocolate4', 'darkSalmon', 'deepskyblue', 'lightgreen']


def paint(sides):
    t.color(choice(colors))
    for _ in range(sides):
        t.forward(100)
        t.right(360 / sides)


for x in range(3, 11):
    paint(x)


s = Screen()
s.exitonclick()
