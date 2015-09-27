#!/usr/bin/env python

import turtle, math

t = turtle.Turtle()
screen = t.getscreen()
t.penup()

for x in range(-10,10):
    y = math.acos(x)
    t.setpos(x,y)
    t.pendown()

turtle.exitonclick()
