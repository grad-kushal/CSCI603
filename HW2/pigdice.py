""" 
file: pigdice.py
language: python3
description: The pigdice game using turtle and score
"""

__author__ = 'Kushal Kale Arujn K'

import math
import random as r
import turtle as t

from score import Keeper

# Width of the window
FRAME_WIDTH = 800

# Height of the window
FRAME_HEIGHT = 800

# Side of the die face
SIDE = 50

# length of diagonal of the die face
DIAGONAL = math.sqrt(SIDE ** 2 + SIDE ** 2)

# Side of the die
HEADER_SIZE = 50

# Dot Size
DOT_SIZE = 5

# Maximum Score
MAX_SCORE = 10

# score keeper
KEEPER = Keeper()


def draw_outline() -> None:
    """
    Draws the outline of the die.
    
    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    t.pencolor('black')
    t.down()
    for _ in range(4):
        t.forward(SIDE)
        t.left(90)
    t.up()


def draw_center_dot() -> None:
    """
    Draw the center dot on the die face.

    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    t.left(45)
    t.forward(DIAGONAL / 2)
    t.dot(DOT_SIZE)
    t.back(DIAGONAL / 2)
    t.right(45)


def draw_two_dots() -> None:
    """
    Draw two dots on the die face.

    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    t.left(45)
    t.forward(DIAGONAL / 3)
    t.dot(DOT_SIZE)
    t.forward(DIAGONAL / 3)
    t.dot(DOT_SIZE)
    t.right(180)
    t.forward(2 * DIAGONAL / 3)
    t.left(135)


def draw_four_dots() -> None:
    """
    Draw four dots on the die face.

    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    draw_two_dots()
    t.left(90)
    t.forward(SIDE)
    t.left(180)
    draw_two_dots()
    t.forward(SIDE)
    t.left(90)


def draw_six_dots() -> None:
    """
    Draw six dots on the die face.

    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    draw_four_dots()
    t.left(90)
    t.forward(SIDE / 2)
    t.right(90)
    t.forward(1 * SIDE / 3)
    t.dot(DOT_SIZE)
    t.forward(1 * SIDE / 3)
    t.dot(DOT_SIZE)
    t.right(90)
    t.forward(SIDE / 2)
    t.right(90)
    t.forward(2 * SIDE / 3)
    t.right(180)


def draw_die(pips) -> None:
    """
    Draw pips on the die face based on the input.

    :param pips:    number of pips to be drawn
    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """

    assert 1 <= pips <= 6

    if pips % 2 == 1:
        draw_center_dot()

    if pips == 2 or pips == 3:
        draw_two_dots()
    elif pips == 4 or pips == 5:
        draw_four_dots()
    elif pips == 6:
        draw_six_dots()


def clear_die() -> None:
    """
    Clear the die face.

    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    t.color('white')
    t.begin_fill()
    draw_outline()
    t.end_fill()


def do_nothing(x, y) -> None:
    """
    A function to be returned as an empty on-click handler

    :param x:       x coordinate
    :param y:       y coordinate
    :return:        None
    """
    pass


def draw_rectangle(length, width) -> None:
    """
    Draw a rectangle.

    :param length:      length of the rectangle
    :param width:       width of the rectangle
    :pre:               pos(0, width / 2),
                        (relative to the rectangle)
                        facing east, up
    :post:              pos(0, width / 2),
                        (relative to the rectangle)
                        facing east, up
    :return:            None
    """
    t.begin_fill()
    t.left(90)
    t.forward(width / 2)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(width / 2)
    t.right(90)
    t.end_fill()
    t.up()
    t.color('black')


def erase_area(length, width) -> None:
    """
    Erase a rectangular area.

    :param length:      length of the rectangular area to be  erased
    :param width:       width of the rectangular area to be erased
    :pre:               pos(0, width / 2),
                        (relative to the rectangle)
                        facing east, up
    :post:              pos(0, width / 2),
                        (relative to the rectangle)
    :return:            None
    """
    t.color('white')
    t.begin_fill()
    draw_rectangle(length, width)
    t.color('black')


def play_turn(keeper, x, y) -> None:
    """
    Roll a die for the current player and update scores.
    
    :param keeper:      instance of the score.Keeper object
    :param x:           x-coordinate of the point clicked
    :param y:           y-coordinate of the point clicked 
    :return:            None
    """

    # check if HOLD is clicked
    if (SIDE / 10 <= x <= SIDE * 1.2)  \
            and (-HEADER_SIZE * 1.5 <= y <= -HEADER_SIZE):
        game_over = False
        # current player won, game over
        if keeper.score[keeper.player] + keeper.points >= MAX_SCORE:
            game_over = True
            # switch player so that current player's total score is updated
            keeper.switch_player()
            
        keeper.switch_player()
        if game_over:
            update_scoreboard(
                str(keeper.player + 1),
                keeper.score[keeper.player]
            )
        else:
            update_scoreboard(
                "1" if 1 - keeper.player == 0 else "2",
                keeper.score[keeper.player - 1]
            )

    else:
        die_throw = r.randint(1, 6)
        draw_die(die_throw)
        if die_throw != 1:
            # update points
            keeper.add_points(die_throw)
        else:
            # set points of current turn to zero
            keeper.points = 0
            keeper.switch_player()
            update_scoreboard(
                "1" if 1 - keeper.player == 0 else "2",
                keeper.score[keeper.player - 1]
            )

    show_prompt(keeper.player)
    update_turn_total(keeper.points)
    clear_die()


def update_turn_total(turn_total) -> None:
    """
    Update the turn total message.
    
    :param turn_total:      turn total to be updated
    :return:                None
    """
    t.left(90)
    t.forward(HEADER_SIZE * 2 + SIDE)

    # clear previous turn total
    t.left(90)
    t.forward(SIDE)
    t.right(180)
    erase_area(3 * SIDE, HEADER_SIZE)
    t.forward(SIDE)

    # write the turn total
    t.forward(SIDE / 2)
    t.write("Turn Total: " + str(turn_total), align="center",
            font=("Calibri", 13, "bold"))

    # go to pos(0, 0)
    t.right(180)
    t.forward(SIDE / 2)
    t.left(90)
    t.forward(HEADER_SIZE * 2 + SIDE)
    t.left(90)


def draw_hold_button() -> None:
    """
    Draw the "HOLD" button.
    
    :pre:           pos(0, 0), facing east, up
    :post:          pos(0, 0), facing east, up
    :return:        None
    """
    t.speed(9)
    t.right(90)
    t.forward(HEADER_SIZE * 1.5)

    t.left(90)
    t.forward(SIDE / 10)
    t.write("HOLD", font=("Calibri", 13, "bold"))
    t.up()

    # go to pos(0, 0)
    t.left(180)
    t.forward(SIDE / 10)
    t.right(90)
    t.forward(HEADER_SIZE * 1.5)
    t.right(90)


def show_prompt(player_number) -> None:
    """
    Show prompt of which player's turn it is. If game is over, display winner.

    :param player_number:       number corresponding to the player, as
                                specified in the score.Keeper object
    :pre:                       pos(0, 0), facing east, up
    :post:                      pos(0, 0), facing east, up
    :return: 
    """
    t.left(90)
    t.forward(HEADER_SIZE + SIDE)

    # clear the previous prompt
    t.left(90)
    t.forward(SIDE)
    t.right(180)
    erase_area(3 * SIDE, HEADER_SIZE)
    t.forward(SIDE)

    t.forward(SIDE / 2)

    # construct the prompt message
    player = "Player {}".format(player_number + 1)
    if KEEPER.score[player_number] >= MAX_SCORE:
        prompt_msg = player + " has won!"
    else:
        prompt_msg = player + "'s turn"
        
    # write the prompt message
    t.write(
        prompt_msg, 
        align="center",
        font=("Calibri", 10, "normal")
    )
    
    # go back to pos(0,0)
    t.right(180)
    t.forward(SIDE / 2)
    t.left(90)
    t.forward(HEADER_SIZE + SIDE)
    t.left(90)


def play(x, y) -> None:
    """
    Used as a mouse click event handler. Plays a turn for the current player
    
    :param x:       x-coordinate of the point clicked
    :param y:       y-coordinate of the point clicked
    :return:        None
    """
    t.onscreenclick(do_nothing)
    play_turn(KEEPER, x, y)
    t.onscreenclick(play)

    if KEEPER.score[0] >= MAX_SCORE or KEEPER.score[1] >= MAX_SCORE:
        t.onscreenclick(do_nothing)
        

def update_scoreboard(player: str, score: int) -> None:
    """
    Update the score board.
    
    :param player:      player whose score is to be updated
    :param score:       score to be displayed
    :pre:               pos(0, 0), facing east, up
    :post:              pos(0, 0), facing east, up
    :return:            None
    """
    t.left(90)
    t.forward(FRAME_HEIGHT / 2 - HEADER_SIZE / 2)
    if player == "1":
        t.left(90)
    else:
        t.right(90)

    # clear previous scores
    t.forward(FRAME_WIDTH / 2)
    t.left(180)
    print(">>>>>>>>>", player, score)
    erase_area(
        FRAME_WIDTH / 2,
        HEADER_SIZE * 0.9)
    t.forward(FRAME_WIDTH / 6)

    t.write(
        f"Player {player}: " + str(score),
        font=("Calibri", 15, "bold"),
        align="center"
    )

    # go back to pos(0, )
    t.forward(FRAME_WIDTH / 3)
    t.setheading(270)
    t.forward(FRAME_HEIGHT / 2 - HEADER_SIZE / 2)
    t.left(90)


def draw_header(height) -> None:
    """
    Draw the topmost part of the window to contain the scoreboard.

    :param  height:     height of the header
    :pre:               pos(0, 0), facing east, up
    :post:              pos(0, 0), facing east, up
    :return:            None
    """
    t.left(90)
    t.forward(FRAME_HEIGHT / 2 - height)
    t.left(90)
    t.forward(FRAME_WIDTH / 2)
    t.left(180)
    t.down()
    t.forward(FRAME_WIDTH)
    t.left(180)
    t.up()
    t.forward(FRAME_WIDTH / 2)
    t.left(90)
    t.forward(FRAME_HEIGHT / 2 - height)
    t.left(90)


def init_scoreboard() -> None:
    """
    Initialize the scoreboard by drawing the header and setting the players'
    initial scores on the board.

    :pre:               pos(0, 0), facing east, up
    :post:              pos(0, 0), facing east, up
    :return:            None
    """
    draw_header(HEADER_SIZE)
    update_scoreboard("1", KEEPER.score[0])
    update_scoreboard("2", KEEPER.score[1])


def init_gameplay(keeper) -> None:
    """
    Initialize gameplay by drawing score board, hold button, and the die.

    :param keeper:      instance of the score.Keeper object
    :pre:               pos(0, 0), facing east, up
    :post:              pos(0, 0), facing east, up
    :return:            None
    """
    t.speed(0)
    t.hideturtle()
    t.setup(FRAME_WIDTH, FRAME_HEIGHT)
    t.up()
    init_scoreboard()
    draw_hold_button()
    update_turn_total(keeper.points)
    show_prompt(keeper.player)
    draw_outline()


def main() -> None:
    init_gameplay(KEEPER)
    t.onscreenclick(play)
    t.mainloop()


if __name__ == "__main__":
    main()
    