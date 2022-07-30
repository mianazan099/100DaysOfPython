# import colorgram
# colors = colorgram.extract('image.jpg', 84)
# colors_list = []
# for n in range(len(colors)):
#     values = colors[n].rgb
#     r = values.r
#     g = values.g
#     b = values.b
#     colors_list.append((r, g, b))
# print(colors_list)

import turtle
import random

x = -225
y = x
colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
          (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
turtle.colormode(255)
jim = turtle.Turtle()
jim.speed(0)
jim.penup()
for n in range(10):
    jim.setpos(y, x)
    x += 50
    for n in range(10):
        jim.dot(20, random.choice(colors))
        jim.forward(50)
jim.hideturtle()
turtle.done()
