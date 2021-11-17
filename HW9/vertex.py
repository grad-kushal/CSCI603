"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS

An implementation of a vertex as part of a graph.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

import math
from typing import Union

class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = 'coordinates', 'connectedTo', 'shortest_escape_length'

    def __init__(self, coordinates: tuple[int, int]):
        """
        Initialize a vertex
        :param coordinates: The identifier for this vertex
        :return: None
        """
        self.coordinates = coordinates
        self.connectedTo = {}
        self.shortest_escape_length = math.inf

    def addNeighbor(self, nbr, weight=0):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.coordinates)

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]

    def get_shortest_escape_length(self) -> Union[float, int]:
        """
        Get the length of the shortest path from this vertex to the escape.

        @return:        the shortest path from this vertex to the escape
        """
        return self.shortest_escape_length

    def get_shortest_escape_length(self, shortest_escape_length) -> None:
        """
        Set the length of the shortest path from this vertex to the escape.

        @return:        None
        """
        self.shortest_escape_length = shortest_escape_length


def testVertex():
    """
    A test function for the Vertex class.
    :return: None
    """
    vertexA = Vertex('A')
    vertexB = Vertex('B')
    vertexC = Vertex('C')
    vertexD = Vertex('D')
    vertexA.addNeighbor(vertexB, 3)
    vertexA.addNeighbor(vertexC, 1)
    vertexB.addNeighbor(vertexA, 4)
    vertexB.addNeighbor(vertexC, 2)
    vertexC.addNeighbor(vertexD, 5)

    # test __str__()
    print(vertexA)
    print(vertexD)

    # test getWeight()
    print('A -> B weight (3):', vertexA.getWeight(vertexB))
    print('C -> D weight (5):', vertexC.getWeight(vertexD))

    # test getConnections():
    print("B's neighbors ():", [vertex.id for vertex in vertexB.getConnections()])
    print("D's neighbors ():", list(vertexD.getConnections()))

if __name__ == '__main__':
    testVertex()
