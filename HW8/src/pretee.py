"""
CSCI-603 PreTee Lab
Author: RIT CS
Author: {YOUR NAMES HERE}

The main program and class for a prefix expression interpreter of the
PreTee language.  See prog1.pre for a full example.

Usage: python3 pretee.py source-file.pre
"""

import sys  # argv
import literal_node  # literal_node.LiteralNode
import variable_node  # variable_node.VariableNode
import assignment_node  # assignment_node.AssignmentNode
import print_node  # print_node.PrintNode
import math_node  # math_node.MathNode
import syntax_error  # syntax_error.SyntaxError
import runtime_error  # runtime_error.RuntimeError


class PreTee:
    """
    The PreTee class consists of:
    :slot srcFile: the name of the source file (string)
    :slot symTbl: the symbol table (dictionary: key=string, value=int)
    :slot parseTrees: a list of the root nodes for valid, non-commented
        line of code
    :slot lineNum:  when parsing, the current line number in the source
        file (int)
    :slot syntaxError: indicates whether a syntax error occurred during
        parsing (bool).  If there is a syntax error, the parse trees will
        not be evaluated
    """
    __slots__ = 'srcFile', 'symTbl', 'parseTrees', 'lineNum', 'syntaxError'

    # the tokens in the language
    COMMENT_TOKEN = '#'
    ASSIGNMENT_TOKEN = '='
    PRINT_TOKEN = '@'
    ADD_TOKEN = '+'
    SUBTRACT_TOKEN = '-'
    MULTIPLY_TOKEN = '*'
    DIVIDE_TOKEN = '//'
    MATH_TOKENS = ADD_TOKEN, SUBTRACT_TOKEN, MULTIPLY_TOKEN, DIVIDE_TOKEN

    def __init__(self, srcFile):
        """
        Initialize the parser.
        :param srcFile: the source file (string)
        """
        self.srcFile = srcFile
        self.lineNum = 0
        self.parseTrees = []
        self.symTbl = {}

    def __parse(self, tokens):
        """
        The recursive parser that builds the parse tree from one line of
        source code.
        :param tokens: The tokens from the source line separated by whitespace
            in a list of strings.
        :exception: raises a syntax_error.SyntaxError with the message
            'Incomplete statement' if the statement is incomplete (e.g.
            there are no tokens left and this method was called).
        :exception: raises a syntax_error.SyntaxError with the message
            'Invalid token {token}' if an unrecognized token is
            encountered (e.g. not one of the tokens listed above).
        :return:
        """

        # base case - when no tokens are left ot process
        if not tokens:
            return None

        # get the first token in the list
        token = tokens[0]

        # remove it from the list
        del tokens[0]

        # when token is an identifier, return a variable node
        if token.isidentifier():
            return variable_node.VariableNode(token, self.symTbl)

        # when token is a number
        if token.isdigit():
            return literal_node.LiteralNode(int(token))

        # when token is "="
        if token == self.ASSIGNMENT_TOKEN:
            variable = self.__parse(tokens)
            expression = self.__parse(tokens)

            # add variable to the symbol table
            self.symTbl[variable.id] = expression.evaluate()

            return assignment_node.AssignmentNode(
                variable,
                expression,
                self.symTbl,
                self.ASSIGNMENT_TOKEN
            )

    def parse(self):
        """
        The public parse is responsible for looping over the lines of
        source code and constructing the parseTree, as a series of
        calls to the helper function that are appended to this list.
        It needs to handle and display any syntax_error.SyntaxError
        exceptions that get raised.
        : return None
        """

        # read the raw lines from the file
        with open(self.srcFile) as f:
            raw_lines = [line.strip() for line in f.readlines()]

        # build a parse tree corresponding to each line
        for line in raw_lines:

            self.lineNum += 1

            # skip over comment lines
            if not line.startswith(self.COMMENT_TOKEN):

                # tokenize the lines
                tokens = line.split(" ")

                # build a parse tree for this line
                tree = self.__parse(tokens)
                if tree is None:
                    # TODO: should something be done here?
                    pass
                else:
                    self.parseTrees.append(tree)

    def emit(self):
        """
        Prints an infix string representation of the source code that
        is contained as root nodes in parseTree.
        :return None
        """
        for tree in self.parseTrees:
            print(tree.emit())

    def evaluate(self):
        """
        Prints the results of evaluating the root notes in parseTree.
        This can be viewed as executing the compiled code.  If a
        runtime error happens, execution halts.
        :exception: runtime_error.RunTimeError may be raised if a
            parse tree encounters a runtime error
        :return None
        """
        pass


def main():
    """
    The main function prompts for the source file, and then does:
        1. Compiles the prefix source code into parse trees
        2. Prints the source code as infix
        3. Executes the compiled code
    :return: None
    """
    if len(sys.argv) != 2:
        print('Usage: python3 pretee.py source-file.pre')
        return

    pretee = PreTee(sys.argv[1])
    print('PRETEE: Compiling', sys.argv[1] + '...')
    pretee.parse()
    print('\nPRETEE: Infix source...')
    pretee.emit()
    print('\nPRETEE: Executing...')
    try:
        pretee.evaluate()
    except runtime_error.RuntimeError as e:
        # on first runtime error, the supplied program will halt execution
        print('*** Runtime error:', e)


if __name__ == '__main__':
    main()
