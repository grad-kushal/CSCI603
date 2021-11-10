"""
CSCI-603 Parser Lab
Author: RIT CS
Author: Kushal Kale         (ksk7657@rit.edu)
        Arjun Kozhissery    (ak8913@rit.edu)

A math expression is of the prefix form:

    '{operator} {left-expression} {right-expression}'

For example:

    '+ 10 20'
    '* 3 5'
    '- 2 4'
    '// 13 2'
    '+ 2 * 8 7'

When emitted, the statement is converted into an infix string:

    '(10 + 20)'
    '(3 * 5)'
    '(2 - 4)'
    '(13 //2 )'
    '(2 + (8 * 7))'

When evaluated, integer result is returned:

    30
    15
    -2
    6
    58

A runtime exception is raised division by 0 is attempted:

    '// 4 0'            # error message: Division by zero error
"""

import runtime_error  # runtime_error.RuntimeError
import pretee  # pretee.PreTee.ADD_TOKEN, ...
import literal_node
import variable_node
import syntax_error


class MathNode:
    """
    A MathNode consists of:
    :slot left: the left expression (LiteralNode, MathNode, VariableNode)
    :slot right: the right expression (LiteralNode, MathNode, VariableNode)
    :token: the character for the math operation (str)
    """
    __slots__ = 'left', 'right', 'token'

    def __init__(self, left, right, token):
        """
        Initialize a MathNode.
        :param left: the left expression (LiteralNode, MathNode, VariableNode)
        :param right: the right expression (LiteralNode, MathNode, VariableNode)
        :param token: the character for the math operation (str)
        :return: None
        """
        if not isinstance(left, (literal_node.LiteralNode,
                                 MathNode, variable_node.VariableNode)):
            raise syntax_error.SyntaxError("Bad math operation")
        if not isinstance(right, (literal_node.LiteralNode, MathNode,
                                  variable_node.VariableNode)):
            raise syntax_error.SyntaxError("Bad math operation")

        self.left = left
        self.right = right
        self.token = token

    def emit(self):
        """
        Returns a parenthesized string with the emits of the left and
        right expressions, e.g.:
            '({left-emit} {token} {right-emit})'
        :return:
        """
        result = "(" + self.left.emit() + " " \
                 + str(self.token) + " "\
                 + self.right.emit() + ")"
        return result

    def evaluate(self):
        """
        Evaluates the math expression and returns the result.
        :exception: raises a runtime_error.RuntimeError if division by zero
            is attempted, with the message, 'Division by zero error'
        :return: The result of performing the math operation (int)
        """
        if self.token == pretee.PreTee.ADD_TOKEN:
            return self.left.evaluate() + self.right.evaluate()
        elif self.token == pretee.PreTee.SUBTRACT_TOKEN:
            return self.left.evaluate() - self.right.evaluate()
        elif self.token == pretee.PreTee.MULTIPLY_TOKEN:
            return self.left.evaluate() * self.right.evaluate()
        else:
            if self.right.evaluate() != 0:
                return self.left.evaluate() // self.right.evaluate()
            else:
                raise runtime_error.RuntimeError("Division by zero error.")
