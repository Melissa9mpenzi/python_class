from turtle import Turtle
#inbuit module
#freedom module
from random import random
#helps in getting random numbers
t = Turtle()
for i in range(100):
    step = int(random()*100)
    angle = int(random()*360)
    t.right(angle)
    t.forward(step)