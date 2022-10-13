from turtle import *
import random
import sys
import time
from math import *
t=Turtle()
t1=Turtle()
t1.shapesize(2,2)
t2=Turtle()
t3=Turtle()
t4=Turtle()
t4.penup()
t4.color("Lightgreen")
t4.shape("square")
t4.shapesize(2,2)
t3.color("Lightgreen")
t2.penup()
t2.color("Lightgreen")
t2.shape("circle")
s=Screen()
t1.penup()
def k1():
    t1.lt(90)
def k2():
    t1.rt(90)
def dist(x,y,z,w):
    t=(x-z)**2+(y-w)**2
    return(sqrt(t))
#s.bgcolor(0.2,0.5,0.2)
s.bgcolor("Lightgreen")
s.setup(width=500,height=500,startx=0,starty=0)
t.penup()
t.goto(-220,-220)
t.pendown()
t.width(10)
t.setheading(90)
t.fd(440)
t.setheading(0)
t.fd(440)
t.setheading(270)
t.fd(440)
t.setheading(180)
t.fd(440)
t1.color("Blue")
t1.speed(1)
c=0
v=0
a=random.randint(-218,218)
b=random.randint(-218,218)
p=random.randint(-180,180)
q=random.randint(-180,180)
t4.goto((p,q))
t2.goto((a,b))
t2.color("red")
while(True):
    t1.fd(2)
    k=dist(t1.xcor(),t1.ycor(),p,q)
    if((t1.xcor()>=220 or t1.xcor()<=-220 or t1.ycor()>=220 or t1.ycor()<=-220) or k<=20):
        t2.color("Lightgreen")
        t3.pensize(25)
        t3.color("red")
        t3.penup()
        t3.goto(-30,-30)
        t3.pendown()
        t3.write("GAME OVER")
        m= str("your score= ")+str(c)
        t3.penup()
        t3.goto(-30,-10)
        t3.pendown()
        t3.write(m)
        t3.color("Lightgreen")
        t3.penup()
        t3.goto((-30,-45))
        j=str("high score=")+str(v)
        t3.pendown()
        t3.color("red")
        t3.write(j)
        s.delay(15000)
        break
    s.onkey(k1,"Left")
    s.onkey(k2,"Right")
    s.listen()
    d=dist(t1.xcor(),t1.ycor(),a,b)
    print(d)
    if(d<=8):
        t2.color("Lightgreen")
        a=random.randint(-200,200)
        b=random.randint(-200,200)
        c=c+5
        t2.goto((a,b))
        t2.color("Red")
        t4.color("Lightgreen")
        t4.goto((p,q))
        t4.color("brown")
    if(v<=c):
        v=c
    if(c>=20):
        t1.speed(10)
    if(c>=40):
        t1.speed(10)
s.exitonclick("Enter")

