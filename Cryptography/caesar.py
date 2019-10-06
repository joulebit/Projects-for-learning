# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:02:58 2019

@author: Joule
"""

from cipher import Cipher
import random

class Caesar(Cipher):
    """push the symbols key steps to the right"""

    def encode(self, text, key):
        encoded = ''
        for letter in text:
            encoded += self.dictionary.get((ord(letter)-32+key)%95)
        return encoded

    def decode(self, coded_text, key):
        decoded = ''
        for letter in coded_text:
            decoded += self.dictionary.get((ord(letter)-32-key)%95)
        return decoded

    def generate_key(self):
        return random.randint(1,94)
    """forbedre verify funksjonen"""
