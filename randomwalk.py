import turtle as t
import random

tim = t.Turtle()
turtle_color = ["Maroon", "PaleTurquoise", "Green", "Red", "Magenta", "SaddleBrown",
                "OliveDrab",
                "DarkSlateGray", "IndianRed", "Gray", "Black", "OrangeRed"]
tim.pensize(10)
tim.speed("fastest")
walk = [0, 90, 180, 270]

for _ in range(200):
    tim.color(random.choice(turtle_color))
    tim.forward(30)
    tim.setheading(random.choice(walk))
