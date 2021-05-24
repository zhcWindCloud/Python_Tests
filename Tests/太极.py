from turtle  import *
pensize(3)
speed(8)
pendown()
circle(100,180)
circle(200,180)
circle(100,-180)
fillcolor('black')
begin_fill()
circle(100,180)
circle(200,180)
circle(100,-180)
end_fill()
penup()
goto(0,100)
dot(50)
goto(0,-100)
pencolor('white')
dot(50)
hideturtle()



import turtle
turtle.speed(10)
t = turtle.Pen()
turtle.bgcolor("black")
sides=eval(input("输入要绘制的边的数目，请输入2-6的数字！"))
colors=["red","yellow","green","blue","orange","purple"]
for x in range(20):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

import turtle
t = turtle.Pen()
turtle.bgcolor("black")


my_name=turtle.textinput("输入你的姓名","你的名字？")
colors=["red","yellow","green","blue","orange","purple"]
for x in range(100):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x*6)
    t.pendown()
    t.write(my_name,font=("Arial",int((x+6)/6),"bold"))
    t.left(92)

