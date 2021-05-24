'''import turtle
turtle.pensize(2)
turtle.color("yellow","red")
d =0

for i in range(100):
    turtle.seth(d)
    d +=177
    turtle.fd(135)



from turtle import *
begin_fill()
color("yellow","red")
pensize(2)
left(50)
fd(110)
left(3)
fd(3)
circle(50,180)
right(110)
circle(50,180)
left(10)
fd(1)
left(3)
fd(130)
end_fill()'''
    

import time
from turtle import *
pensize(2)
speed(10)
def shit():
    right(1)
    fd(1)
    return

def Dra():
    begin_fill()
    color("yellow","yellow")
    pendown()
    for i in range(5):
        fd(35)
        right(144)
    end_fill()
    return 
def Dra1():
    begin_fill()
    color("yellow","yellow")
    pendown()
    for i in range(5):
        fd(15)
        right(144)
    end_fill()
    return
speed(3)
#心形
begin_fill()
color("red","red")
left(20)
#fd(5)
circle(180,56)
shit()
circle(60,180)
right(150)
circle(60,180)
shit()
circle(180,55)
left(20)
end_fill()


#五角星
pensize(1)
penup()
goto(-105,150)
Dra()
penup()
goto(-60,175)
left(65)
Dra1()
penup()
goto(-40,155)
right(25)
Dra1()
penup()
goto(-40,125)
right(35)
Dra1()
penup()
goto(-60,100)
right(30)
Dra1()
hideturtle()


'''
from turtle import *

def Dra():
    penup()
    goto(-280,120)
    begin_fill()
    pendown()
    color("yellow","yellow")
    pendown()
    for i in range(5):
        fd(35)
        right(144)
    end_fill()
    return

def Dra1():
    pendown()
    begin_fill()
    color("yellow","yellow")
    for i in range(5):
        fd(15)
        right(144)
    end_fill()
    return

pensize(3)
begin_fill()
color("yellow","red")
for i in range(2):
    left(90)
    fd(180)
    left(90)
    fd(300)
end_fill()
pensize(1)
Dra()
penup()
goto(-230,150)
left(60)
Dra1()
penup()
goto(-210,130)
right(15)
Dra1()

penup()
goto(-210,100)
right(45)
Dra1()


penup()
goto(-230,80)
right(30)'''
Dra1()

time.sleep(3)
