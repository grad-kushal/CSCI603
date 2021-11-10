"""
CSCI-603 Parser Lab
Author: RIT CS

A custom exception class for representing a runtime error.
"""


class RuntimeError(Exception):

    def __init__(self, message):
        super().__init__(message)
