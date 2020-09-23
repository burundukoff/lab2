import turtle
n = int(input("введите n\n"))
a = int(input("введите a\n"))
b = a
turtle.shape('turtle')
turtle.speed(1)
for line in range(n):
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    a = a + b//2