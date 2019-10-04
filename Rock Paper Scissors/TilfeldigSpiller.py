# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:00:33 2019

@author: Joule
"""
import random as rn
from Spiller import Spiller

class Tilfeldig(Spiller):
    """Tilfeldig spiller"""
    def __init__(self, name):
        super().__init__(name)
    def velg_aksjon(self):
        return rn.randint(0, 2)
