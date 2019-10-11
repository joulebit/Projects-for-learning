# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:16:40 2019

@author: Joule
"""

from container import Container

class Queue(Container):
    """queue class for storing items"""

    def __init__(self):
        Container.__init__(self)

    def peek(self):
        """peek at the first item in the list"""
        if not self.is_empty():
            return self.items[0]
        return None

    def pop(self):
        """pop the first item"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
