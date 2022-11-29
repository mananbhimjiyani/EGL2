import turtle as t
from turtle import Screen
import math


def egldrawing():
    TL = float(input("Please enter the length of the line(TL):- "))
    TV = float(input("Please enter the top view of the line(TV):- "))
    FV = float(input("Please enter the front view of the line(FV):- "))
    d = float(input("Please enter the distance above the reference line:- "))
    e = float(input("Please enter the distance below the reference line:- "))

    angle1 = math.acos(TV / TL)
    angle1 = math.degrees(angle1)
    angle2 = math.acos(FV / TL)
    angle2 = math.degrees(angle2)

    TL=TL*2
    FV=FV*2
    TV=TV*2
    e=e*2
    d=d*2

    t.left(90)
    t.forward(d)
    t.right(90)
    t.forward(FV)
    t.back(FV)
    t.left(angle1)
    print(f"Theta is {angle1}")
    t.forward(TL)
    x = t.xcor()
    t.right(angle1)
    t.forward(100)
    t.write("Locus of a")
    t.back(300)
    t.forward(200)
    t.write("b1'")
    t.left(angle1)
    t.back(TL)
    t.right(angle1)
    t.left(90)
    t.goto(0, 0)
    t.back(e)
    t.right(90)
    # Drawing of TV
    t.forward(TV)
    t.back(TV)
    t.right(angle2)
    print(f"PHI is {angle2}")
    t.forward(TL)
    t.left(angle2)
    t.forward(100)
    t.write("Locus of b")
    t.back(300)
    t.forward(200)
    t.write("a1'")
    x1 = t.xcor()
    t.right(angle2)
    t.back(TL)
    t.left(angle2)
    t.penup()
    t.goto(x, 0)
    t.right(90)
    t.forward(e)
    t.pendown()
    t.circle(-(TV),90)
    t.penup()
    t.goto(x1, 0)
    t.right(90)
    t.forward(d)
    t.pendown()
    t.circle(FV,90)
    op=math.sin(angle2)
    H1=op*TV
    total1=H1+d
    t.penup()
    t.goto(52.5,71.13939*2.5)
    t.write("b'")
    t.pendown()
    t.goto(0,d)
    t.pu()
    t.goto(52.5,71.13939*2.5)
    t.left(90)
    t.pd()
    t.forward(71.13939*2.5)
    op=math.sin(angle1)
    H2=op*FV
    t.forward(e)
    t.goto(25.5*2,-71.13939*1.9)
    t.write("b2   ",align='right')
    t.goto(0,-e)





screen = Screen()
t.screensize(10000, 10000)
t.title("EGL PROJECT")
t.pen(speed=5)
t.penup()
t.goto(-100, 0)
t.write("X")
t.pendown()
t.forward(200)
t.write("Y")
t.penup()
t.goto(0, 0)
t.pendown()
egldrawing()
t.exitonclick()
