import turtle
import numpy
turtle.shape('turtle')
turtle.speed(1)
n = 10
quantity_corner = 3
lenght = 100
# n = int(input("введите количество многоугольников\n"))
# start_quantity_corner = int(input("введите количество углов стартового многоугольника\n"))
# start_lenght = int(input("Введите стартовый размер стороны\n"))



def polygon(lenght, quantity_corner, corner):
    for i in range(quantity_corner):
        turtle.forward(lenght)
        turtle.left(corner)



def  turn(corner):
    turtle.right(90-corner)


def corner(quantity_corner):
    if quantity_corner > 3:
        corner1 = 180-(180 * (quantity_corner - 2))/quantity_corner
    else:
        corner1 = 120
    return corner1


def r_circle(lenght):
    r_circle1 = lenght * (2 * numpy.sin(360/(2 * numpy.pi)))
    return r_circle1


def go_to(lenght, corner1, corner2):
    #turtle.penup()

    turtle.right(90 + 0.5 * corner1)
    turtle.forward(r_circle(lenght) * 0.2 - r_circle(lenght))
    turtle.right(corner2)
 #   turtle.forward(lenght * 0.2)
 #   turtle.right(180)
    #turtle.pendown()
#    turtle.left(corner(quantity_corner))
    #current_lenght = current_lenght*1.2
    #return current_lenght




for i in range(n):
    corner1 = corner(quantity_corner)
    polygon(lenght, quantity_corner, corner1)
    quantity_corner += 1
    a = 1
    corner2 = corner(quantity_corner)
    go_to(lenght, corner1, corner2)
    lenght = lenght * 1.2
    #turn(current_corner)










