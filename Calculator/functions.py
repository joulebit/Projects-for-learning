# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:43:14 2019

@author: Joule
"""
import numbers

class Function:
    """class for functions"""
    def __init__(self, func):
        self.func = func

    def execute(self, element, debug=True):
        """execute function on element"""
        if not isinstance(element, numbers.Number):
            raise TypeError("Cannot execute func if element is not a number")
        result = self.func(element)
        if debug is True:
            print("Function: " + self.func.__name__
                  + "({:f}) = {:f}".format(element, result))
        return result
