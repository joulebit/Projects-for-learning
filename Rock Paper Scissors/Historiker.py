# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:18:09 2019

@author: Joule
"""
import random as rn
from Spiller import Spiller

class Historiker(Spiller):
    """Må finne en matchende tidligere substring i
    en mutert kopi av enemy_choices listen"""

    def __init__(self, name, husk):
        super().__init__(name)
        self.husk = husk
        self.action = []
        self.enemy_choices = []


    def velg_aksjon(self):

        def random_action():
            """Tilfeldig valg"""
            choice = rn.randint(0, 2)
            self.action.append(choice)
            return choice

        if((len(self.enemy_choices) < self.husk*2) or (self.husk <= 0)):
            """husk*2 kommer fra at vi har n siste resultat vi har som
            mønstret våres, og da må vi minst ha n andre resultater
            å se på for å lete etter mønsteret"""
            return random_action()

        else:

            following_move = [0, 0, 0]
            """Holder oversikt over hvor ofte ett
            trekk taes som følger etter sekvensen"""

            nmy_choices = self.enemy_choices.copy()
            huske_moves = self.enemy_choices.copy()

            del nmy_choices[-self.husk:]
            """Kutter opp listene til å representere de ulike navnene"""
            del huske_moves[:-self.husk]


            ln_husk = len(huske_moves)
            for i in range(len(nmy_choices) - ln_husk + 1):
                """Trenger bare å sjekke opp til
                de indeksene som kan inneholde antall elementer sub_list har"""
                if all(huske_moves[j] == nmy_choices[i+j] for j in range(self.husk)):
                    following_move[self.enemy_choices[i+self.husk]] += 1



            if sum(following_move) == 0:
                """ingen gjenkjente mønster --> tilfeldig"""
                return random_action()

            else:
                enemy_next_move = 0
                for index in range(1, 3):
                    if following_move[index] > following_move[enemy_next_move]:
                        """Finn hvilke av de tre valgene som dukker
                        opp flest ganger etter sekvensen"""
                        enemy_next_move = index

                best_move = (enemy_next_move + 1)%3
                self.action.append(best_move)
                return best_move


    def motta_resultat(self, result):
        """Nesten samme motta_resultat logikk som MestVanlig strategien"""
        if result == 0.5:
            enemy_choice = self.action[-1]

        elif result == 1:
            enemy_choice = (self.action[-1] - 1)%3

        elif result == 0:
            enemy_choice = (self.action[-1] +1)%3

        self.enemy_choices.append(enemy_choice)
