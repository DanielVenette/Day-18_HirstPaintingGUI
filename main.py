# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     color_list.append((red, green, blue))
#
# print(color_list)

from turtle import Turtle, Screen
import random

leonardo = Turtle()
screen = Screen()

#set turtle shape/color
leonardo.shape("turtle")
leonardo.color("green")
leonardo.penup()
leonardo.speed(1)
screen.colormode(255)
leonardo.hideturtle()

# list of colors in painting
new_color_list = [(25, 109, 165), (195, 38, 81), (237, 161, 51), (234, 215, 86), (227, 237, 229), (223, 137, 176),
                  (144, 108, 57), (103, 195, 218), (205, 166, 30), (20, 57, 132), (212, 74, 92), (239, 89, 50),
                  (141, 208, 227), (119, 192, 140), (5, 186, 176), (106, 108, 199), (138, 29, 73), (4, 161, 86),
                  (98, 51, 36), (23, 156, 210), (227, 168, 186), (175, 185, 220), (230, 170, 163), (158, 210, 187),
                  (29, 90, 96), (91, 46, 31), (242, 208, 8)]

#set starting position
x = -250
y = -250
leonardo.setposition(x, y)

#draw 100 dots
counter = 0
for _ in range(100):
    color = random.choice(new_color_list)
    print(color)
    leonardo.dot(20, color)
    leonardo.forward(50)
    counter += 1
    #every 10 dots, go up and start another row
    if counter == 10:
        y += 50
        leonardo.setposition(x,y)
        counter = 0


screen.exitonclick()


