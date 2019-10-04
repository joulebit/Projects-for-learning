# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:22:47 2019

@author: Joule
"""

from MangeSpill import MangeSpill
from EnkeltSpill import EnkeltSpill
from Historiker import Historiker
from MestVanlig import MestVanlig
from Sekvensiell import Sekvensiell
from TilfeldigSpiller import Tilfeldig



fortsett = True


def contestant(input_string):
    """finn ut hvilken spiller som skal initialiseres"""
    if input_string == "1":
        return Tilfeldig("Jon")

    if input_string == "2":
        return Sekvensiell("Henrik")

    if input_string == "3":
        return MestVanlig("Ivar")

    if input_string == "4":
        husk = input("hvor mange trekk på rad ønsker du at spilleren skal se etter mønster på?\n")
        return Historiker("Kasper", int(husk))

while fortsett:
    p1 = input("Velkommen til Rock Paper Scissors game simulator\nDo you want to choose the first player to be:\n[1] Random player\n[2] Sequencial player\n[3] Analyzing Most Common\n[4] Historian\n")
    player1 = contestant(p1)

    p2 = input("And the second player?\n")
    player2 = contestant(p2)

    antall = input("Hvor mange spill ønsker du å ha i turneringen?\n")

    if int(antall) < 2:
        EnkeltSpill(player1, player2).gjennomfoer_spill()

    else:
        MangeSpill(player1, player2, int(antall)).arranger_turnering()
