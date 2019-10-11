# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:27:47 2019

@author: Joule
"""

class Container:
    """Superclass for queue and stack"""

    def __init__(self):
        self.items = []

    def size(self):
        """return the size of the list"""
        return len(self.items)

    def is_empty(self):
        """check if the list is empty"""
        return not bool(len(self.items))

    def push(self, item):
        """add a new item in the end of the list"""
        self.items.append(item)

    def pop(self):
        """pop the next item to be chosen.
        The first for queue and last for stack"""
        pass

    def peek(self):
        """look at the next item in the line without altering it"""
        pass
