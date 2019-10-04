# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:55:11 2019

@author: Joule
"""

from Aksjon import Aksjon

class EnkeltSpill:
    """Singelt spill"""

    def __init__(self, spiller1, spiller2):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.vinner = None
        self.action1 = None
        self.action2 = None

        self.points = None

    def gjennomfoer_spill(self):
        """utfør spillet og gi respons til spillerne med resultatet"""
        self.action1 = Aksjon(self.spiller1.velg_aksjon())
        self.action2 = Aksjon(self.spiller2.velg_aksjon())

        if self.action1 == self.action2:
            self.spiller1.motta_resultat(0.5)
            self.spiller2.motta_resultat(0.5)
            self.vinner = None
            self.points = 0.5

        elif self.action1 > self.action2:
            self.spiller1.motta_resultat(1)
            self.spiller2.motta_resultat(0)
            self.vinner = self.spiller1.oppgi_navn()
            self.points = 1

        else:
            self.spiller1.motta_resultat(0)
            self.spiller2.motta_resultat(1)
            self.vinner = self.spiller2.oppgi_navn()
            self.points = 0

    def __str__(self):
        self.gjennomfoer_spill()
        return(self.spiller1.oppgi_navn() +
               " valgte " + str(self.action1.__str__()) +
               " mens " + self.spiller2.oppgi_navn() + " valgte "
               + str(self.action2.__str__()) + " og vinneren ble " + str(self.vinner))
