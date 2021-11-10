"""
CSCI-603 Parser Lab
Authors: RIT CS
         Arjun Kozhissery    (ak8913@rit.edu)
         Kushal Kale         (ksk7657@rit.edu)

A custom exception class for representing a syntax error.
"""


class SyntaxError(Exception):
    """
    Thrown when the pretree compiler encounters one of the a syntax error.
    """

    def __init__(self, message=""):
        """
        Intializes this exception
        @param message:     Message to be displayed with this exception.
        """
        super().__init__(message)
