# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:47:50 2019

@author: Joule
"""

#https://www.youtube.com/watch?v=9wd50TKv_OQ


class Aksjon:
    """Definerer aksjonene og overloader operatorene = og < slik at du kan sammenligne aksjonene"""
    def __init__(self, move):
        self.move = move

    def __eq__(self, other):
        return self.move == other

    def __gt__(self, other):
        if (self.move - other.move)%3 == 1:
            return True
        return False

    def __str__(self):
        return self.move
    