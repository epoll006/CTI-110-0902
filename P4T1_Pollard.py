import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
olaf = turtle.Pen()
olaf.color("white")
olaf.shape("turtle")
olaf.pensize(3)
olaf.speed(10)

for i in range (10):
    for i in range(2):    
        olaf.forward(100)
        olaf.right(60)
        olaf.forward(100)
        olaf.right(120)
    olaf.right(36)
