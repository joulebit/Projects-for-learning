# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:01:53 2019

@author: Joule
"""
from calculator import Calculator.functions
import re

class Text_parser:
    """"""
    def __init__(self):
        self.translated=[]


    def translate(self, text):
        """"""
        self.text= text.replace(" ", "").upper()
        
        floats = "^[-1234567890.]+|"
        functions = "|".join(["^" + func for func in Calculator().functions.keys()])
        
        operators = "|".join(["^" + operator for operator in Calculator().operators.keys()])
        

        

        while len(self.text) > 0:
            check_float = re.search(floats,self.text)
            check_func = re.search(functions,self.text)
            check_oper = re.search(operators,self.text)
            if check_float.end(0) > 0:
                print(check_float.group(0))
                self.translated.append(float(check_float.group(0)))
                self.text = self.text[check_float.end(0):]
            elif check_func:
                print(check_func.group(0))
                self.translated.append(Calculator().functions.get(check_func.group(0)))
                self.text = self.text[check_func.end(0):]
            elif check_oper:
                print(check_oper.group(0))
                self.translated.append(Calculator().operators.get(check_oper.group(0)))
                self.text = self.text[check_oper.end(0):]
            
        
        return self.translated
a = Text_Parser()
a.translate(input("Skriv inn regnestykket: "))
print(a.translated)

        