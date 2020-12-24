from turtle import Turtle, Screen

t = Turtle()

for _ in range(4):
    t.right(90)
    t.fd(100)

screen = Screen()
screen.exitonclick()
