# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 21:52:32 2019

@author: Joule
"""
from stack import Stack
from functions import Function
from operators import Operator
from queues import Queue

class RPN_solver:
    """solve a given RPN list"""

    def __init__(self):
        self.tall = Stack()

    def solve(self, elements):
        """solve the given RPN sequence"""
        for element in elements:
            if isinstance(element, (float, int)):
                self.tall.push(element)
            elif isinstance(element, Function):
                last_element = self.tall.pop()
                new_element = element.execute(last_element)
                self.tall.push(new_element)
            elif isinstance(element, Operator):
                tall2 = self.tall.pop()
                tall1 = self.tall.pop()
                new_element = element.execute(tall1, tall2)
                self.tall.push(new_element)

        return self.tall.peek()


class RPN_converter:
    """convert a list of numbers and operations and functions to RPN format"""

    def __init__(self):
        self.operators = Stack()
        self.output = Queue()
        self.out = []

    def convert(self, elements):
        """convert given list to RPN format"""
        for element in elements:
            if isinstance(element, (float, int)):
                self.output.push(element)
            elif isinstance(element, Function):
                self.operators.push(element)
            elif element == "(":
                self.operators.push(element)
            elif element == ")":
                while self.operators.peek() != "(":
                    self.output.push(self.operators.pop())
                self.operators.pop()
            elif isinstance(element, Operator):
                while self.operators.peek() != None or self.operators.peek() != "(":
                    if isinstance(self.operators.peek(), Operator) and \
                    self.operators.peek() > element:
                        self.output.push(self.operators.pop())
                    else:
                        break
                self.operators.push(element)

        while self.operators.peek() != None:
            self.output.push(self.operators.pop())


        return self.output.items
