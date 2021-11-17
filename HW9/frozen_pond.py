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
from typing import Optional
from vertex import Vertex


class FrozenPond:
    """A class that represents a frozen pond"""

    __slots__ = (
        'input_file',  # input file path
        'height',  # height of the pond
        'width',  # width of the pond
        'escape_row',  # row in which the pond can be escaped
        'pond_raw',  # raw representation of the pond (list of list of str)
        'pond_graph',  # graph representation of the frozen pond
        'escape_vertex'  # vertex in which escape is possible
    )

    def __init__(self, input_file):
        """
        Initializes the pond object
        @param input_file:      input file path
        """
        self.input_file = input_file
        self._process_input_file()
        self.pond_graph = self._build_graph()

    def _process_input_file(self):
        """
        Process the input file to get the attributes like height, width,
        and escape row from the file, and build the raw representation of the
        pond.

        @return:        None
        """
        pond = []
        try:
            with open(self.input_file) as f:

                lines = f.readlines()

                # extract pond dimensions and escape row
                dimensions = lines.pop(0).split()
                self.height = int(dimensions[0])
                self.width = int(dimensions[1])
                self.escape_row = int(dimensions[2])

                # Create raw pond representation
                for line in lines:
                    row = line.split()
                    pond.append(row)

                self.pond_raw = pond

        except FileNotFoundError as _:
            print("Filename not found %s" % self.input_file)
            exit(1)

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
        current_row = row
        current_column = column

        if direction == 0:

            # find the stopping row
            for r in range(row - 1, -1, -1):
                if self.pond_raw[r][current_column] == '*':
                    break
                else:
                    current_row = r

        elif direction == 1:

            # find the stopping column
            for c in range(column + 1, self.width):

                if self.pond_raw[current_row][c] == '*':
                    break
                else:
                    current_column = c

        elif direction == 2:

            # find the stopping row
            for r in range(row + 1, self.height):

                if self.pond_raw[r][current_column] == '*':
                    break
                else:
                    current_row = r

        elif direction == 3:

            # find the stopping column
            for c in range(column - 1, -1, -1):
                if self.pond_raw[current_row][c] == '*':
                    break
                else:
                    current_column = c

        return current_row, current_column

    def _build_graph(self) -> Graph:
        """
        Builds a graph representation of the pond.

        @return:
        """

        graph = Graph()

        # build a vertex from each coordinate
        for x in range(0, self.width):
            for y in range(0, self.height):

                # make sure this coordinate is not a rock
                if self.pond_raw[x][y] != '*':

                    # add the vertex to the graph
                    vertex = graph.addVertex((x, y))

                    if x == self.escape_row and y == self.width - 1:
                        self.escape_vertex = vertex

                    # get the stopping coordinates along each direction
                    for direction in range(0, 4):
                        stop_x, stop_y = self._find_stopping_coordinates(
                            x, y, direction
                        )

                        # if stop coordinates are not the current coordinates
                        if (stop_x, stop_y) != (x, y):
                            graph.addEdge((x, y), (stop_x, stop_y))
        return graph

    def _bfs(self,
             start: Vertex,
             destination: Vertex) -> Optional[list[Vertex]]:
        """
        Do a breadth first search to check if there is a path between start
        and destination.

        @param start:           start vertex
        @param destination:     destination vertex
        @return:                list representing the path if a path is
                                present between the start and destination,
                                else returns None
        """
        # queue to enforce a visiting order based on hop distance
        q = [start]

        # dictionary to keep track of visited nodes
        # along with their predecessors
        visited = {start: None}

        while len(q) > 0:
            current_vertex = q.pop(0)

            # destination vertex found
            if current_vertex == destination:
                break

            # add neighboring vertices to the queue
            for nbr in current_vertex.getConnections():
                if nbr not in visited:
                    visited[nbr] = current_vertex
                    q.append(nbr)

        if destination in visited:
            shortest_path = []
            temp = destination
            while temp != start:
                shortest_path.insert(0, temp)
                temp = visited[temp]
            shortest_path.insert(0, start)
            return shortest_path
        else:
            return None

    def print_escape_paths(self) -> None:
        """
        Prints the escape paths in the ascending order of length.

        @return:        None
        """
        vertices = self.pond_graph.getVertices()
        escape_paths = {}

        for vertex in vertices:

            path = self._bfs(self.pond_graph.getVertex(vertex),
                             self.escape_vertex)

            if path is not None:
                path_length = len(path)
                try:

                    # even though the path only contains one vertex,
                    # we'll still need to do one hop to escape from the
                    # escape vertex
                    if self.pond_graph.getVertex(vertex) == \
                            self.escape_vertex:

                        # to offset the subtraction done in the subsequent step
                        path_length = path_length + 1

                    escape_paths[path_length - 1].append(vertex)
                except KeyError:
                    escape_paths[path_length - 1] = [vertex]

            else:
                try:
                    escape_paths["No path"].append(vertex)
                except KeyError:
                    escape_paths["No path"] = [vertex]

        # retrieve the values in the key 'No path' to be printed in the end
        no_path_vertices = None
        if "No path" in escape_paths:
            no_path_vertices = escape_paths["No path"]
            del escape_paths["No path"]

        # print the vertices is ascending order or escape path length
        lengths = escape_paths.keys()

        for length in sorted(lengths):
            print(length, ":", [(x, y) for (x, y) in escape_paths[length]])

        # print vertices with no path to the escape
        if no_path_vertices:
            print("No path : ", no_path_vertices)


def run_tests():
    """
    Run thr test cases for this program.

    @return:    None
    """

    from pprint import pprint  # for printing dict

    input_file_format = 'test{}.txt'
    output_file_format = 'out{}.txt'

    # run the 3 test cases test2.txt to test4.txt
    for i in range(2, 5):

        print("*" * 50)

        input_file = input_file_format.format(i)
        print("Running test case in", input_file)
        output_file = output_file_format.format(i)

        # get the expected result
        with open(output_file) as o:
            expected_dict = eval(o.read())
            print("\nExpected result:")
            pprint(expected_dict)

        # print the actual result
        print("\nActual result:")
        fp = FrozenPond(input_file)
        fp.print_escape_paths()

        print("*" * 50, '\n')


def main() -> None:
    """
    Runs the program on the given example and additional test cases.

    @return:    None
    """

    print("Running program on the given example: test1.txt")
    fp = FrozenPond('test1.txt')

    # print the escape path
    fp.print_escape_paths()

    # run additional test cases
    print('\n\nRunning additional test cases')
    run_tests()


if __name__ == '__main__':
    main()
