
from turtle import *

speed("slow")


def arm():
    for i in range(16):
        a = 20 * (i % 20) + 50
        forward(a)
        backward(a)

        right(360/120)


def star():
    for i in range(15):
        print(arm())


print(star())
exitonclick()
