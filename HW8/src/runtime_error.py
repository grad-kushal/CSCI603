"""
CSCI-603 Parser Lab
Author: RIT CS
        Arjun Kozhissery    (ak8913@rit.edu)
        Kushal Kale         (ksk7657@rit.edu)

A custom exception class for representing a runtime error.
"""


class RuntimeError(Exception):
    """
    Thrown when the pretree compiler encounters one of the following errors:
        - unrecognized variable
        - division by zero

    """
    
    def __init__(self, message):
        """
        Intializes this exception
        @param message:     Message to be displayed with this exception
        """
        super().__init__(message)
