import turtle

turtle.shape('turtle')
turtle.speed(10)

def cicle(turn):

    for i in range(360):
        turtle.forward(1)
        turtle.left(turn)


for i in range(3):
    cicle(1)
    cicle(-1)
    turtle.left(60)