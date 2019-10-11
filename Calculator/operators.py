# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:52:32 2019

@author: Joule
"""
import numbers

class Operator:
    """class for operators"""
    def __init__(self, operator, strength):
        self.operator = operator
        self.strength = strength

    def execute(self, element1, element2, debug=True):
        """execute given operator on two elements"""
        if (not isinstance(element1, numbers.Number)) or (not isinstance(element2, numbers.Number)):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.operator(element1, element2)

        if debug is True:
            print("Function: " + self.operator.__name__
                  + "({:f},{:f}) = {:f}".format(element1, element2, result))
        return result


    def __gt__(self, other):
        """to compare the strength of different operators"""
        if self.strength > other.strength:
            return True
        return False

    def get_operator(self):
        """return the operator of the object"""
        return self.operator
