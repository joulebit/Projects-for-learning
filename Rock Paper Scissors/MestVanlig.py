# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:21:08 2019

@author: Joule
"""

import random as rn
from Spiller import Spiller


class MestVanlig(Spiller):
    """Lagrer klassens valg og holder en tally over
    hvor mange ganger en motstander har valgt en
    spesifikk trekk"""

    def __init__(self, name):
        super().__init__(name)
        self.action = []
        self.total_enemy = [0, 0, 0]


    def velg_aksjon(self):
        """Hvis objektet ikke har noen historikk over motstanderen,
        så velger den tilfeldig"""
        if sum(self.total_enemy) == 0:
            choice = rn.randint(0, 2)
            self.action.append(choice)
            return choice

        top_enemy_index = 0
        for i  in range(1, 3):
            if self.total_enemy[i] > self.total_enemy[top_enemy_index]:
                top_enemy_index = i

        """velger det som slår motstanderens mest vanlige valg"""
        top_choice = (top_enemy_index + 1)%3
        self.action.append(top_choice)
        return top_choice



    def motta_resultat(self, result):
        """Bruker mine valg pluss resultatet for å finne
        ut hva motstanderen valgte"""
        if result == 0.5:
            enemy_choice = self.action[-1]

        elif result == 1:
            enemy_choice = (self.action[-1] - 1)%3

        elif result == 0:
            enemy_choice = (self.action[-1] +1)%3


        """Legger det motstanderen valgte til i tallyen"""
        self.total_enemy[enemy_choice] += 1
