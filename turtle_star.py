import turtle
n = int(input("введите\n"))
turtle.shape('turtle')
turtle.speed(5)
for line in range(n):
    turtle.forward(50)
    turtle.stamp()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180+360/n)
