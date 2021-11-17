"""
Filename:       frozen_pond.py
Description:    Assignment for Lab 9 of CSCI 603

                This program builds a graph corresponding to the given
                representation of a frozen pond and for each vertex in this
                graph, finds the length of the shortest escape path.

Language:       Python 3
Author:         Arjun Kozhissery    (ak8913@rit.edu)
                Kushal Kale         (ksk7657@rit.edu)
"""

from graph import Graph
from queue import Queue
from typing import Optional
from vertex import Vertex


class FrozenPond:
    """A class that represents a frozen pond"""

    __slots__ = (
        'input_file',   # input file path
        'height',       # height of the pond
        'width',        # width of the pond
        'escape_row',   # row in which the pond can be escaped
        'pond_raw',     # raw representation of the pond (list of list of str)
        'pond_graph'    # graph representation of the frozen pond
    )

    def __init__(self, input_file):
        """
        Initializes the pond object
        @param input_file:      input file path
        """
        self.input_file = input_file

    def _process_input_file(self):
        """
        Process the input file to get the attributes like height, width,
        and escape row from the file, and build the raw representation of the
        pond.

        @return:        None
        """
        # for example, the raw representation should look something like this:
        # [
        #   [ '.', '.', '*', '.'],
        #   [ '.', '.', '.', '*'],
        #   [ '.', '.', '.', '.'],
        #   [ '*', '*', '.', '.'],
        # ]
        pass

    def _find_stopping_coordinates(self, row, column, direction):
        """
        Look for the coordinates in which one can stop when travelling in a
        straight line from the given coordinates along one of the four
        directions (left, right, up, down). One can stop when one reaches one of
        the edges of the pond or a rock.

        @param row:         row of the coordinate from where one starts
        @param column:      row of the coordinate from where one starts
        @param direction:   0 for up, 1 for right, 2 for down, and 3 for left
        @return:            stopping row, stopping column
        """
        # make use of the raw representation for this traversal
        # trivial case: when the starting position is on the edge of the pond
        # or nearby a rock. For instance, starting from  (0, 0), the stopping
        # coordinate along the left (and up) direction is (0, 0).
        #
        pass

    def _build_graph(self) -> Graph:
        """
        Builds a graph representation of the pond.

        @return:
        """
        # make use of _find_stopping_coordinates
        pass

    def _bfs(self,
             start: Vertex,
             destination: Vertex,
             visited: set[str]) -> Optional[list[Vertex]]:
        """
        Do a breadth first search to check if there is a path between start
        and destination.

        @param start:           start vertex
        @param destination:     destination vertex
        @param visited:         vertices visited so far
        @return:                list representing the path if a path is
                                present between the start and destination,
                                else returns None
        """
        # standard BFS algo
        pass

    def print_escape_paths(self) -> None:
        """
        Prints the escape paths in the ascending order of length.

        @return:        None
        """

        #
        # something like this:
        # for all vertices in the graph:
        #   path_nodes = _bfs(start, destination):
        #   escape_paths = dict()
        #   if path_nodes:
        #      path_length = len(path_nodes) - 1
        #        update in escape_paths dictionary
        #   else:
        #       update in escape_paths dictionary under the key 'No path'
        #
        #
        pass


def main():
    pass

if __name__ == '__main__':
    main()

