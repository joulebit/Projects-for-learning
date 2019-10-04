# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:20:37 2019

@author: Joule
"""

class Spiller:
    """Spiller er en superclass for de senere spillertypene"""
    def __init__(self, name):
        self.name = name

    def velg_aksjon(self):
        """metode for å velge aksjon"""
        pass

    def motta_resultat(self, result):
        """Hva skal skje når man mottar et resultat"""
        pass

    def oppgi_navn(self):
        """må kunne oppgi navnet sitt"""
        return self.name
