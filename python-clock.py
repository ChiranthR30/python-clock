import turtle as tr
import time
import tkinter as tk


wn = tr.Screen()
wn.bgcolor("black")
wn.setup(width=1000, height=600)
wn.title("Analogue Clock")
wn.tracer(0)


pen = tr.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_circle(pen,r,fillcolor=False,col="white"): #col - pencolor
    if fillcolor==True:
        pen.up()
        pen.goto(0,r)
        pen.setheading(180)
        pen.pensize(2)
        pen.color(col)
        pen.pendown()
        pen.fillcolor(col)
        pen.begin_fill()
        pen.circle(r)
        pen.end_fill()

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)
    else:
        pen.up()
        pen.goto(0,r)
        pen.setheading(180)
        pen.pensize(2)
        pen.color(col)
        pen.pendown()
        pen.circle(r)

        pen.penup()
        pen.goto(0,0)
        pen.setheading(90)

def draw_line(pen,col="white"):

    i=0
    while i < 12:
        pen.color(col)
        pen.fd(170)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        i+=1
    
    j=0
    while j < 60:
        pen.color(col)
        pen.fd(190)
        pen.pendown()
        pen.fd(10)
        pen.penup()
        pen.goto(0,0)
        pen.rt(6)
        j+=1



def min_hand(pen,m):
    
    pen.up()
    pen.goto(0,0)
    pen.color("white")
    pen.pensize(3)
    pen.setheading(90)
    angle=(m/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(140)

def sec_hand(pen,s):

    pen.up()
    pen.goto(0,0)
    pen.color("red")
    pen.pensize(5)
    pen.setheading(90)
    angle=(s/60)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(160)

def hour_hand(pen,h):

    pen.up()
    pen.goto(0,0)
    pen.color("white")
    pen.pensize(4)
    pen.setheading(90)
    angle=(h/12)*360
    pen.rt(angle)
    pen.pendown()
    pen.bk(20)
    pen.fd(100)

pen.color('yellow')
pen.penup()
pen.goto(0,135)
pen.write("12", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(150,-14)
pen.write("3", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(0,-160)
pen.write("6", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(-150,-13)
pen.write("9", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(75,110)
pen.write("1", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(138,57)
pen.write("2", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(136,-85)
pen.write("4", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(80, -135)
pen.write("5", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(-75, -143)
pen.write("7", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(-125, -84)
pen.write("8", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(-82, 116)
pen.write("11", align="center", font=("Courier", 20, "normal"))

pen.penup()
pen.goto(-120, 60)
pen.write("10", align="center", font=("Courier", 20, "normal"))

#def print_num():



while True:
    h=int(time.strftime("%I"))
    m=int(time.strftime("%M"))
    s=int(time.strftime("%S"))

    draw_circle(pen,200)
    draw_circle(pen,220)
    draw_circle(pen,5,True,"white")
    draw_line(pen)
    min_hand(pen,m)
    sec_hand(pen,s)
    hour_hand(pen,h)

    wn.update()
    time.sleep(1)
    pen.clear()

wn.mainloop()
