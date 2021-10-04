""" 
file: score.py
language: python3
description: Holds a class whose instances keep scores for a Pig Dice game
"""

__author__ = 'James Heliotis'


class Keeper:
    """
    A score keeper for a 2-player game.
    The only "rule" this class knows is that points are accumulated
    within a player's turn until it's the other player's turn.
    """

    __slots__ = "player", "points", "score"
    player: int
    points: int
    score: list

    def __init__(self: "Keeper") -> "Keeper":
        """
        Create a score keeper.
        :return: None
        """
        self.player = 0
        self.points = 0
        self.score = [0, 0]

    def add_points(self: "Keeper", p: int) -> None:
        """
        Add more potential points for the current player
        :param p: the number of points to be added
        :return: None
        """
        self.points += p

    def switch_player(self: "Keeper") -> None:
        """
        Add any accumulated points to the current player's score.
        Make the other player to the be current player, who starts at
        no accumulated points.
        :return: None
        """
        self.score[self.player] += self.points
        self.points = 0
        self.player = 1 - self.player


def test() -> None:
    keeper = Keeper()
    for points in 5, 3, 2, 2, 'H', \
                  6, 6, 3, 4, 'H', \
                  4, 6, 6, 1, \
                  5, 4, 3, 4, 5, 'H', \
                  2, 2, 2, 5, 6, 'H', \
                  1, \
                  4, 5, 6, 3, 6, 6, 'H':
        if points == 'H':
            keeper.switch_player()
        elif points == 1:
            keeper.points = 0
            keeper.switch_player()
        else:
            keeper.add_points(points)
    for player in range(2):
        print("Player " + str(player) + "'s score = " + \
              str(keeper.score[player]))


if __name__ == '__main__':
    test()
