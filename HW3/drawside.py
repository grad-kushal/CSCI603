import turtle
import math

def drawside(length, level, theta):
    cumulative_length = 0
    if level == 1 :
        cumulative_length += length
        turtle.forward(length)
    else:
        cumulative_length += drawside(length/4, 1, theta)
        turtle.left(theta)
        cumulative_length += drawside(length/(4*math.cos(math.radians(theta))), level - 1, theta)
        turtle.right(theta * 2)
        cumulative_length += drawside(length/(4*math.cos(math.radians(theta))), level - 1, theta)
        turtle.left(theta)
        cumulative_length += drawside(length/4, 1, theta)
    return cumulative_length

turtle.up()
turtle.left(180)
turtle.forward(100)
turtle.right(180)
turtle.down()
print(drawside(500, 7, 45))
turtle.mainloop()