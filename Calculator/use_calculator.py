# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:15:56 2019

@author: Joule
"""
from calculator import Calculator


inp = " "
c = Calculator()

while input:
    inp = input("Hva ønsker du å regne ut: ")
    result = c.calculate_expression(inp)
    print(result)