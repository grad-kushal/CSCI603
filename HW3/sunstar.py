"""
Filename:       sunstar.py
Description:    Assignment for Lab 3 of CSCI 603

                This program draws a polygon with a particular pattern for
                the sides sides.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

import math
import turtle as t


def init_canvas(sides: int, length: int) -> None:
    """
    Initialize the canvas to draw the polygon in.
    :return:
    """

    t.speed(0)
    t.setworldcoordinates(
        -sides * length / 2,
        -sides * length / 2,
        sides * length / 2,
        sides * length / 2
    )


def draw_side(level: int, angle: float, length: float) -> float:
    """
    Draw a side of the polygon.

    :param level:       number of levels to draw
    :param angle:       deviation angle in radians
    :param length:      length of the side
    :pre:               pos(0, 0), relative to the start of the line, down
    :pre:               pos(side, 0), relative to the start of the line, down

    :return:            cumulative length of the sides drawn
    """

    if level == 1:  # base case
        t.forward(length)
        return length

    total_length = 0
    total_length += draw_side(1, angle, length / 4)
    steep_side = length / (4 * math.cos(math.radians(angle)))
    t.left(angle)
    total_length += draw_side(level - 1, angle, steep_side)
    t.right(2 * angle)  # angle to rotate = 180 - ( 180 - (2 * angle))
    total_length += draw_side(level - 1, angle, steep_side)
    t.left(angle)
    total_length += draw_side(1, angle, length / 4)
    return total_length


def draw_polygon(sides: int, level: int, angle: float, length: float) -> float:
    """
    Draw a polygon where each side corresponding to the drawing of a side
    :param sides:       number of sides to draw
    :param level:       number of levels to draw
    :param angle:       deviation angle in radians
    :param length:      length of the side
    :pre:               pos(0, 0), down
    :pre:               pos(0, 0), relative to the start of the line, down

    :return:            cumulative length of the sides drawn
    """
    interior_angle = 180 * (sides - 2) / sides

    total_length = 0
    t.left(interior_angle)
    while sides > 0:
        total_length += draw_side(level, angle, length)
        t.right(180 - interior_angle)
        sides -= 1

    t.right(interior_angle)
    return total_length

def get_positive_integer(prompt: str) -> int:
    while True:
        try:
            input_value = int(input(prompt))
        except ValueError:
            print("Invalid Input. An integer is expected")
            continue
        if input_value < 0:
            print("Invalid Input. A positive number is expected")
            continue
        else:
            break
    return input_value
    
def get_integer(prompt: str) -> int:
    input_value = None
    while True:
        try:
            input_value = int(input(prompt))
        except ValueError:
            print("Invalid Input. An integer is expected")
            continue
        if input_value != None:
            break
    return input_value

def input_values():
    """
    Takes input for drawing a polygon
    :return:        a tuple containg the required input
    """
    sides = get_positive_integer("Enter the number of sides: ")
    length = get_positive_integer("Enter the length of the initial side: ")
    levels = get_positive_integer("Enter the number of levels: ")
    angle = 0
    if levels > 1:
        angle = get_integer("Enter the deflection angle: ")
    
    return sides, length, levels, angle

def main() -> None:
    """
    Draws a polygon based on the input parameters provided by the user
    :return:        None
    """
    
    sides, length, levels, angle  = input_values()

    init_canvas(sides, length)
    total_length = draw_polygon(sides, levels, angle, length)

    print("Total length of the polygon is ", total_length)
    t.mainloop()


if __name__ == '__main__':
    main()

