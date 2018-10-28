import turtle
wn = turtle.Screen()
wn.bgcolor("purple")
don = turtle.Pen()
amy = turtle.Pen()
don.shape("turtle")
amy.shape("turtle")
don.color("green")
amy.color("red")
don.pensize(4)
amy.pensize(4)



don.speed(5)
amy.speed(5)

i = 0

while i < 7:
    don.forward(100)
    don.left(90)
    i = i+1

    don.right(180)
    amy.backward(200)
    amy.right(120)
    i = i+1
    


