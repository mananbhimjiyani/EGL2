import turtle as t
from turtle import Screen
import math


def prjectionOfLine():
    t.penup()
    t.goto(-100, 0)
    t.write("X")
    t.pendown()
    t.forward(200)
    t.write("Y")
    t.penup()
    t.goto(0, 0)
    t.pendown()

    TL = 70
    TV = 45
    FV = 60
    d = 35
    e = 30

    angle1 = math.acos(TV / TL)
    angle1 = math.degrees(angle1)
    angle2 = math.acos(FV / TL)
    angle2 = math.degrees(angle2)

    TL = TL * 2
    FV = FV * 2
    TV = TV * 2
    e = e * 2
    d = d * 2

    t.left(90)
    t.forward(d)
    t.right(90)
    t.forward(FV)
    t.back(FV)
    t.pensize(5)
    t.left(angle1)
    print(f"Theta is {angle1}")
    t.forward(TL)
    x = t.xcor()
    t.right(angle1)
    t.pensize(1)
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
    t.pensize(5)
    t.forward(TL)
    t.left(angle2)
    t.pensize(1)
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
    t.circle(-(TV), 90)
    t.penup()
    t.goto(x1, 0)
    t.right(90)
    t.forward(d)
    t.pendown()
    t.circle(FV, 90)
    op = math.sin(angle2)
    H1 = op * TV
    total1 = H1 + d
    t.penup()
    t.goto(52.5, 71.13939 * 2.5)
    t.write("b'")
    t.pendown()
    t.goto(0, d)
    t.pu()
    t.goto(52.5, 71.13939 * 2.5)
    t.left(90)
    t.pd()
    t.forward(71.13939 * 2.5)
    op = math.sin(angle1)
    H2 = op * FV
    t.forward(e)
    t.goto(25.5 * 2, -71.13939 * 1.9)
    t.write("b2   ", align='right')
    t.goto(0, -e)

def projectionOfTriangle():
    t.heading()

    t.pensize(4)
    t.forward(700)

    t.penup()
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(500)

    t.pendown()

    t.pensize(3)

    t.right(30)
    t.forward(160)
    t.left(120)
    t.forward(160)
    t.left(120)
    t.forward(160)

    t.pensize(1)

    t.right(120)
    t.forward(300)

    t.pensize(3)

    t.right(90)
    ##bottom line###
    t.forward(138.56)

    t.pensize(1)

    t.right(90)

    t.forward(300)

    t.penup()

    t.right(90)
    t.forward(370)

    t.left(60)
    t.forward(80)

    t.pendown()

    t.pensize(3)

    t.right(120)
    t.forward(160)
    t.right(120)
    t.forward(160)
    t.right(120)
    t.forward(160)

    t.right(120)
    t.forward(160)

    t.pensize(1)

    t.right(30)
    t.forward(230)

    t.pensize(3)

    t.right(90)
    t.forward(160)

    t.pensize(1)

    t.right(90)
    t.forward(230)

    t.right(30)
    t.forward(160)

    t.right(150)
    t.forward(368.56)



screen = Screen()
t.screensize(10000, 10000)
t.title("EGL PROJECT")
t.pen(speed=5)
print(
    "Q1 A line AB 70 mm long, has its end A 35 mm above HP and 30 mm in front of VP. The top view and front view has a length of 45 mm and 60 mm respectively. Draw its projections. ")
print(
    "Q2 an equilateral triangle plane ABC of side 160mm has its plane parallel to VP and 20mm away from it. Draw its projections when of it's side is perpendicular to HP,parallel to HP")

x = int(input("Please enter the number of question:- (where 1 is for Q1 2 for Q2 respectively) "))
if x == 1:
    prjectionOfLine()
elif x == 2:
    projectionOfTriangle()

t.exitonclick()
