# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:34:28 2019

@author: Joule
"""

import unittest
import numpy as np
from calculator import Calculator, Text_parser
from queues import Queue
from stack import Stack
from rpn import RPN_solver, RPN_converter
from operators import Operator
from functions import Function


class TestCalculator(unittest.TestCase):
    def test_calc_operators(self):
        c = Calculator()
        value = c.calculate_expression("47.03pluss-3")
        self.assertEqual(value, 44.03)
        value = c.calculate_expression("5gange6")
        self.assertEqual(value, 30)
        value = c.calculate_expression("-5minus-9")
        self.assertEqual(value, 4)
        value = c.calculate_expression("15dele5")
        self.assertEqual(value, 3)
    
    def test_calc_functions(self):
        c = Calculator()
        value = c.calculate_expression("sqrt2")
        self.assertAlmostEqual(value, np.sqrt(2))
        value = c.calculate_expression("exp11")
        self.assertAlmostEqual(value, np.exp(11))
        value = c.calculate_expression("log14")
        self.assertAlmostEqual(value, np.log(14))
        value = c.calculate_expression("sin7")
        self.assertAlmostEqual(value, np.sin(7))
        value = c.calculate_expression("cos52")
        self.assertAlmostEqual(value, np.cos(52))
    
    def test_operator_strength(self):
        c = Calculator()
        value = c.calculate_expression("3 pluss 5 gange 2")
        self.assertEqual(value, 13)
        value = c.calculate_expression("2 gange3 pluss 5 gange 2")
        self.assertEqual(value, 16)


    def test_calc_nested_parentheses(self):
        c = Calculator()
        value = c.calculate_expression("(2 pluss 5)gange 7")
        self.assertEqual(value, 49)
        value = c.calculate_expression("exp((3 minus 2)pluss(8 dele (1pluss1)))")
        self.assertEqual(value, np.exp(5))
        value = c.calculate_expression("4 minus(3 minus -1)")
        self.assertEqual(value, 0)
    
    
    
    
    def test_queues(self):
        q = Queue()
        for i in range(1,100):
            q.push(i)
        self.assertEqual(99,q.size())
        self.assertEqual(1,q.peek())
        self.assertEqual(1,q.pop())


    def test_stacks(self):
        q = Stack()
        for i in range(1,100):
            q.push(i)
        self.assertEqual(99,q.size())
        self.assertEqual(99,q.peek())
        self.assertEqual(99,q.pop())
    
    def test_RPN_solve(self):
        r = RPN_solver()
        value = r.solve([1, 2, 3, Operator(np.multiply,1), Operator(np.add,0), Function(np.exp)])
        self.assertEqual(value, np.exp(7))
    
    def test_RPN_convert(self):
        t = RPN_converter().convert([5, Operator(np.multiply,1), "(",1,Operator(np.add,0),2,")"])
        self.assertEqual(t[0], 5)
        self.assertEqual(t[1], 1)
        self.assertEqual(t[2], 2)
        self.assertTrue(isinstance(t[3], Operator))
        self.assertTrue(isinstance(t[4], Operator))
    
    def test_text_parser(self):
        parser = Text_parser()
        parsed = parser.translate("(1pluss2)minus3gange4exp5")
        print(parsed)
        self.assertTrue(1,parsed)