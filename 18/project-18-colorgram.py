import turtle
import colorgram
import random
rgb_colors = []
tur = turtle.colormode(255)
colors = colorgram.extract('spot-painting.jpg', 8)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed('fastest')
t.setheading(225)
t.forward(300)
t.setheading(0)

for i in range(1, 101):
    t.dot(20, random.choice(rgb_colors))
    t.forward(50)

    if i % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = turtle.Screen()
s.exitonclick()
