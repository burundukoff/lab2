import random
import turtle

turtle.shape('turtle')

for i in range(100):
    turn = random.randint(-360, 360)
    forward_t = random.randint(30, 100)
    turtle.forward(forward_t)
    turtle.left(turn)
