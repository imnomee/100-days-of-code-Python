from turtle import Turtle, Screen

t = Turtle()


def paint():
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()


for _ in range(50):
    paint()

s = Screen()
s.exitonclick()
