
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

#心形
begin_fill()
color("yellow","red")
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
goto(-105,145)
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
penup()
goto(-350,0)
pendown()
speed(1)
write("我",font=("楷体",150,"bold"))
hideturtle()
penup()
goto(150,0)
pendown()
write("中国",font=("楷体",150,"bold"))





'''

from turtle import *
pensize(2)
speed(10)
def shit():
    right(1)
    fd(1)
    return

begin_fill()
color("black","red")
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
circle(170,80)
shit()
circle(85,180)
#fd(10)
end_fill()
penup()
goto(-200,60)
pendown()
pensize(4)
begin_fill()
color("black","black")
left(120)
fd(460)
right(90)
fd(5)
left(120)
fd(10)
left(120)
fd(10)
left(120)
fd(5)
hideturtle()
end_fill()'''







