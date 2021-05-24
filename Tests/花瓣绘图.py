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



import turtle as t
t.speed(1)
t.pensize(6)
t.begin_fill()
t.color("red","blue")
for i in range(4):
    t.seth(90 * (i + 1))
    #90,180,270，360
    t.circle(120,90)
    #-90,0,90,180
    t.seth(-90 + i * 90)
    t.circle(120,90)
t.end_fill()





