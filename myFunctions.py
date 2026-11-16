import turtle
bob = turtle.Turtle()

bob.penup()
bob.goto(-300,0)
bob.pendown()

bob.fillcolor("Orangered")
bob.begin_fill()
bob.circle(200)
bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown

jump(0,0)
bob.fillcolor("gray")
bob.begin_fill()
bob.circle(20)
bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown

jump(200,-300)
bob.fillcolor("Light blue")
bob.begin_fill()
bob.circle(100)
bob.end_fill()
