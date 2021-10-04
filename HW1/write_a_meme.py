__author__ = 'ksk'

"""
CSCI-603: First Assignment (week 1)
Author: Kushal Kale (ksk7657@rit.edu)

This is a program that prints a meme involving tom.  It uses
 different character drawing functions that can be re-used.
"""

import turtle
import math

# Width of the window
FRAME_WIDTH = 1000

# Height of the window
FRAME_HEIGHT = 1000

# Width of the character
CHAR_WIDTH = 15

# Height of the character
CHAR_HEIGHT = 15

# Width of the space character
SPACE_WIDTH = 5


def init() -> None:
    """
    Initialize for drawing.  (-5, -15) is in the lower left and
    (255, 45) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    #turtle.setup(FRAME_WIDTH, FRAME_HEIGHT)
    turtle.setworldcoordinates(-5, -500, 500, 500)
    turtle.up()
    turtle.setheading(0)
    # turtle.hideturtle()
    turtle.title('Running Tom')
    turtle.speed(5)


def draw_char_space():
    """
    Draws space
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+SPACE_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.forward(SPACE_WIDTH)


def draw_word_space():
    """
    Draws space between words
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+ 2*SPACE_WIDTH, 0), heading (east), up
    :return: None
    """
    draw_char_space()
    draw_char_space()


def draw_char_M(color: str) -> None:  # Testing optional typehints
    """
    Draws M
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    # turtle.showturtle()
    turtle.down()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(135)
    turtle.forward(CHAR_WIDTH / math.sqrt(2))
    turtle.left(90)
    turtle.forward(CHAR_WIDTH / math.sqrt(2))
    turtle.right(135)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.up()


def draw_char_R(color):
    """
    Draws R
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.down()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(90)
    turtle.forward(CHAR_WIDTH)
    turtle.right(90)
    turtle.forward(CHAR_HEIGHT / 2)
    turtle.right(90)
    turtle.forward(CHAR_WIDTH)
    turtle.left(150)
    turtle.forward(math.sqrt(CHAR_WIDTH ** 2 + (CHAR_HEIGHT / 2) ** 2))
    turtle.left(30)
    turtle.up()


def draw_char_U(color):
    """
    Draws U
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.down()
    turtle.forward(CHAR_WIDTH)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.up()
    turtle.forward(CHAR_WIDTH)
    turtle.left(90)
    turtle.down()
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.up()
    turtle.forward(CHAR_WIDTH)


def draw_char_T(color):
    """
    Draws T
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.forward(CHAR_WIDTH / 2)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.forward(CHAR_WIDTH / 2)
    turtle.back(CHAR_WIDTH / 2)
    turtle.right(180)
    turtle.forward(CHAR_WIDTH / 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)


def draw_char_O(color):
    """
    Draws O
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.pendown()
    turtle.forward(CHAR_WIDTH)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.forward(CHAR_WIDTH)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.penup()
    turtle.left(90)
    turtle.forward(CHAR_WIDTH)


def draw_char_G(color):
    """
    Draws G
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(CHAR_WIDTH)
    turtle.back(CHAR_WIDTH)
    turtle.right(90)
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)
    turtle.forward(CHAR_WIDTH)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT / 2)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT / 4)
    turtle.penup()
    turtle.back(CHAR_HEIGHT / 4)
    turtle.left(90)
    turtle.forward(CHAR_HEIGHT / 2)
    turtle.left(90)


def draw_char_N(color):
    """
    Draws N
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+CHAR_WIDTH, 0), heading (east), up
    :return: None
    """
    turtle.pencolor(color)
    turtle.left(90)
    turtle.down()
    turtle.forward(CHAR_HEIGHT)
    turtle.right(135)
    turtle.forward((CHAR_HEIGHT) * math.sqrt(2))
    turtle.left(135)
    turtle.forward(CHAR_HEIGHT)
    turtle.right(180)
    turtle.up()
    turtle.forward(CHAR_HEIGHT)
    turtle.left(90)


def draw_run(color):
    """
    Draws RUN
    :arg: color to draw in
    :pre: pos (x, 0), heading (east), up
    :post: pos (x+40, 0), heading (east), up
    :return: None
    """
    draw_char_R(color)
    draw_char_space()
    draw_char_U(color)
    draw_char_space()
    draw_char_N(color)


def draw_tom(color):
    """
    Draws TOM
    :arg: color to draw in
    :pre: pos (50, 0), heading (east), up
    :post: pos (90, 0), heading (east), up
    :return: None
    """
    draw_char_T(color)
    draw_char_space()
    draw_char_O(color)
    draw_char_space()
    draw_char_M(color)


def main() -> None:
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (150,0), heading (east), up
    :return: None
    """
    init()
    # color = input("Input Color: ")

    draw_run("green")

    draw_word_space()

    draw_tom("red")

    draw_word_space()

    draw_run("blue")

    draw_word_space()

    turtle.hideturtle()

    turtle.mainloop()


if __name__ == '__main__':
    main()
