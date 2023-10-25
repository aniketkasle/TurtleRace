import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
turtle_color = ["Maroon", "PaleTurquoise", "Green", "GreenYellow", "DodgerBlue", "MidnightBlue", "SaddleBrown",
                "DarkSlateBlue",
                "BlueViolet", "CornflowerBlue", "Gray", "Black", "MediumSlateBlue	"]


def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(turtle_color))
    draw_shape(shape_side_n)
