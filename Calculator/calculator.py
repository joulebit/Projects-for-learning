# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:17:52 2019

@author: Joule
"""
import re
import numpy as np
from functions import Function
from operators import Operator
from rpn import RPN_solver, RPN_converter

class Calculator:
    """calculate a given expression using helper classes"""
    def __init__(self):
        self.functions = {'EXP': Function(np.exp),
                          'LOG': Function(np.log),
                          'SIN': Function(np.sin),
                          'COS': Function(np.cos),
                          'SQRT': Function(np.sqrt)}

        self.operators = {'PLUSS': Operator(np.add, 0),
                          'GANGE': Operator(np.multiply, 1),
                          'DELE': Operator(np.divide, 1),
                          'MINUS': Operator(np.subtract, 0)}

    def calculate_expression(self, txt):
        """return a solved expression"""
        parsed = Text_parser().translate(txt)
        rpn = RPN_converter().convert(parsed)
        solved = RPN_solver().solve(rpn)
        return solved


class Text_parser:
    """Take in human written text and standarize it to be able to solve RPN"""
    def __init__(self):
        self.translated = []
        self.text = None

    def translate(self, text):
        """translate normal text to list of numbers and operators/functions for rpn class"""
        self.text = text.replace(" ", "").upper()
        floats = "^[-1234567890.]+|"
        functions = "|".join(["^" + func for func in Calculator().functions.keys()])
        operators = "|".join(["^" + operator for operator in Calculator().operators.keys()])


        while self.text:
            check_float = re.search(floats, self.text)
            check_func = re.search(functions, self.text)
            check_oper = re.search(operators, self.text)
            if check_float.end(0) > 0:
                self.translated.append(float(check_float.group(0)))
                self.text = self.text[check_float.end(0):]
            elif check_func:
                self.translated.append(Calculator().functions.get(check_func.group(0)))
                self.text = self.text[check_func.end(0):]
            elif check_oper:
                self.translated.append(Calculator().operators.get(check_oper.group(0)))
                self.text = self.text[check_oper.end(0):]
            elif re.search("^[(]", self.text):
                self.translated.append("(")
                self.text = self.text[1:]
            elif re.search("^[)]", self.text):
                self.translated.append(")")
                self.text = self.text[1:]

        return self.translated
