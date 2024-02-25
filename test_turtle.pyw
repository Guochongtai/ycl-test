import turtle
import time
import random
j=0.0
lest=['red','orange','yellow','green','blue','royalblue','purple']
turtle.shape("turtle")
turtle.speed(999999)
for i in range(360):
    j+=1
    turtle.seth(j)
    for i in range(4):
        color=random.choice(lest)
        turtle.pencolor(color)
        turtle.forward(100)
        turtle.left(90)
time.sleep(5)