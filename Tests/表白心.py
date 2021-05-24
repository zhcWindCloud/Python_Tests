from turtle import *
import time
pensize(2)
speed(10)
def shit():
    right(1)
    fd(1)
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
penup()
goto(-230,0)
pendown()
time.sleep(1)
write("I",font=("Courier",150,"bold"))
hideturtle()
penup()
goto(150,0)
pendown()
time.sleep(1)
write("Y",font=("Courier",150,"bold"))

time.sleep(5)
