import turtle

turtle.shape('turtle')
#turtle.speed(0)
turtle.left(90)


def cicle(turn, forward):

    for i in range(360):
        turtle.forward(forward)
        turtle.left(turn)


n = 1
for i in range(10):

    cicle(1, n)
    cicle(-1, n)
    n += 0.1
