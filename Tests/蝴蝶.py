
import turtle as t
t.begin_fill()
t.color("red","yellow")
for i in range(4):
    t.seth(90 * (i + 1))
    #90,180,270，360
    t.circle(200,90)
    #-90,0,90,180
    t.seth(-90 + i * 90)
    t.circle(200,90)
t.end_fill()
t.seth(90)
t.circle(400,30)
t.penup()
t.goto(0,0)
t.pendown()
t.right(30)
t.circle(-400,30)
t.hideturtle()
