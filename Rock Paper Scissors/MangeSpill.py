# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:15:00 2019

@author: Joule
"""
import matplotlib.pyplot as plt
from EnkeltSpill import EnkeltSpill




class MangeSpill:
    """lag et turnerings objekt som kan spille mange
    enkeltkamper mellom to spillere"""


    def __init__(self, spiller1, spiller2, antall_spill):
        self.spiller1 = spiller1
        self.spiller2 = spiller2
        self.antall_spill = antall_spill



    def arranger_enkeltspill(self):
        """Gjennomfører et enkeltspill"""
        new_game = EnkeltSpill(self.spiller1, self.spiller2)
        new_game.gjennomfoer_spill()
        return new_game.points

    def arranger_turnering(self):
        """Gjennomfører antall_spill ganger enkeltspill"""
        score = 0
        avg_score = []
        spillt = []


        width = 0.3
        plt.axis([1, self.antall_spill, 0, 1])
        plt.axhline(y=0.5, linewidth=2, color='r')
        for x in range(10):                                         #Fix the plot horizontaal lines
            plt.axhline(y=x/10, linewidth=width, color='c')

        for x in range(10):
            plt.axvline((int(self.antall_spill/10))*(x+1), linewidth=width, color='m')


        for x in range(self.antall_spill):
            spillt.append(x+1)
            score += self.arranger_enkeltspill()
            avg_score.append(score/spillt[-1])



        plt.plot(spillt, avg_score)              # Draw the final linegraph
        plt.show()
