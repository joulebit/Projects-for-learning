# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:23:35 2019

@author: Joule
"""
import random
from cipher import Cipher
from crypto_utils import modular_inverse

class Multiplikasjon(Cipher):
    """Krypter ved hjelp av multiplikasjons cipheret"""

    def encode(self, text, key):
        encoded = ''
        for letter in text:
            encoded += self.dictionary.get(((ord(letter)-32)*key)%95)
        return encoded

    def decode(self, coded_text, key):
        decoded = ''
        for letter in coded_text:
            decoded += self.dictionary.get(((ord(letter)-32)*(modular_inverse(key, 95)))%95)
        return decoded

    def generate_key(self):
        key = 0

        while True:
            key = random.randint(2, 94)
            if modular_inverse(key, 95):
                return key
