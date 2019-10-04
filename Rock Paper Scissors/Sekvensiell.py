# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:51:21 2019

@author: Joule
"""
import random as rn
from Spiller import Spiller


class Sekvensiell(Spiller):
    """Sekvensiell spiller"""

    def __init__(self, name):
        """holder oversikt over hvilke valg den nettopp
        har tatt, og starter med et tilfeldig valg"""
        super().__init__(name)
        self.count = rn.randint(0, 2)

    def velg_aksjon(self):
        """får den til å velge action sekvensielt mellom(0,1,2)"""
        self.count += 1
        return self.count%3
