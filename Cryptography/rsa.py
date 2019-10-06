# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:45:48 2019

@author: Joule
"""

import random
from cipher import Cipher
from crypto_utils import blocks_from_text, text_from_blocks,\
 generate_random_prime, modular_inverse

class RSA(Cipher):
    """RSA kryptering med primtall"""

    def encode(self, text, key):
        encoded = []
        blokker = blocks_from_text(text, 4)
        for blokk in blokker:
            encoded.append(pow(blokk, key[1], key[0]))
        return encoded

    def decode(self, coded_text, key):
        decoded = ''
        blokker_decoded = []
        for blokk in coded_text:
            blokker_decoded.append(pow(blokk, key[1], key[0]))
        decoded = text_from_blocks(blokker_decoded, 4)
        return decoded

    def generate_key(self):
        p = generate_random_prime(50)
        q = generate_random_prime(50)
        while p == q:
            q = generate_random_prime(50)

        _n = p*q
        phi = (p-1)*(q-1)
        while True:
            e = random.randint(3, phi-1)
            d = modular_inverse(e, phi)
            if d != False:
                return ((_n, e), (_n, d))
