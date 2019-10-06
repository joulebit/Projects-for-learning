# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 20:56:22 2019

@author: Joule
"""
import random
from cipher import Cipher


class Ubrytelig(Cipher):
    """har et kodeord som nøkkel som brukes til å kryptere teksten"""

    def encode(self, text, key):
        encoded = ''
        for index in range(len(text)):
            encoded += self.dictionary.get\
            ((ord(text[index])-32+ord(key[index%(len(key))])-32)%95)
        return encoded

    def decode(self, coded_text, key):
        decoded = ''
        for index in range(len(coded_text)):
            decoded += self.dictionary.get\
            ((ord(coded_text[index])-32-(ord(key[index%(len(key))])-32))%95)
        return decoded

    def generate_key(self):
        _f = open('english_words.txt', "r")
        text = _f.read().split()
        _f.close()
        size = len(text)
        return text[random.randint(0, size-1)]
