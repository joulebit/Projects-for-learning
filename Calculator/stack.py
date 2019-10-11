# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:23:22 2019

@author: Joule
"""

from container import Container

class Stack(Container):
    """stack system for storing items"""

    def __init__(self):
        Container.__init__(self)

    def peek(self):
        """peek at the next item in the stack"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def pop(self):
        """pop the next item in the stack"""
        if not self.is_empty():
            return self.items.pop(-1)
        return None
