import turtle
import random
x=150
def square(turtle,x):
    turtle.fd(x)
    turtle.right(90)
def draw():
    x=150
    t=turtle.Turtle()
    t.speed(0)
    t.color("yellow")
    s=turtle.Screen()
    s.colormode(255)
    s.bgcolor("black")
    for i in range(1000):
        r=random.randint(1,255)
        g=random.randint(1,255)
        b=random.randint(1,255)
        t.color(r,g,b)
        square(t,i)
        t.right(5)
        

draw()
    
