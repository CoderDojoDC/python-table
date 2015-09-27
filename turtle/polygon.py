#!/usr/bin/env python3

import sys, turtle
from math import degrees, sin, tan, radians

sides = int(sys.argv[1])
side_len = 2000/sides
radius = side_len / (2 * sin(radians(180/sides)))
apothem = side_len / (2 * tan(radians(180/sides)))
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
print(radius, apothem)

t = turtle.Turtle()
turtle.bgcolor("grey")
t.hideturtle()
t.goto(side_len/2,apothem)
for x in range(sides):
    t.fillcolor(colors[x%7])
    t.begin_fill()
    t.right(360/sides)
    t.forward(side_len)
    t.right((360/sides) + (180-(360/sides))/2)
    t.forward(radius)
    t.end_fill()
    t.right(180)
    t.forward(radius)
    t.left(180)
    t.left((360/sides) + (180-(360/sides))/2)

turtle.done()
