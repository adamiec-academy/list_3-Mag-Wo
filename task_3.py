
from turtle import *
from random import randint

speed("fast")

step = 30
mount = [0, 50, 130, 210, 170, 280, 220, 150, 80, 50, 20, 10, 150, 190, 265, 200, 280, 120, 80, 150, 0]

for i in range(len(mount)):
    goto(i*step, mount[i] + randint(-25,25))
goto(0,0)

exitonclick()
