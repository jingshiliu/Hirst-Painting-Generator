import colorgram
import random
from turtle import Turtle, Screen

arrow = Turtle()
arrow.shape("arrow")
screen = Screen()
screen.colormode(255)

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))


def random_color():
    return random.choice(rgb_colors)


def draw_dot_for_a_row(dots_per_row):
    arrow.penup()
    for i in range(dots_per_row - 1):
        arrow.dot(20, random_color())
        arrow.forward(50)
    arrow.dot(20, random_color())


def draw_hirst_painting(row, col):
    x_position = -25 * col
    y_position = -25 * row
    arrow.speed(0)
    for i in range(row):
        arrow.penup()
        arrow.goto(x_position, y_position)
        draw_dot_for_a_row(col)
        y_position += 50
    arrow.goto(10000,10000)


print("Welcome to hirst-painter!!!\n\n")
row = int(input("How many rows would be in your hirst-painting?"))
col = int(input("How many cols would be in your hirst-painting?"))
draw_hirst_painting(row, col)




screen.exitonclick()