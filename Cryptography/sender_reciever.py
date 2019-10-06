# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:47:22 2019

@author: Joule
"""
from person import Person


class Sender(Person):
    """Sender av kryptert text"""

    def __init__(self):
        Person.__init__(self)
        self.encoded = None
        self.text = None

    def encode(self, text):
        """encode the given text"""
        self.text = text
        self.encoded = self.operate_cipher()

    def get_encoded(self):
        """get the encoded text"""
        return self.encoded

    def operate_cipher(self):
        if(self.cipher and self.key):
            return self.cipher.encode(self.text, self.key)
        return "legg til cipher og key, og prøv igjen"


class Reciever(Person):
    """Mottaker av kryptert text"""
    def __init__(self):
        Person.__init__(self)
        self.decoded = None
        self.text = None

    def decode(self, text):
        """decode the given text"""
        self.text = text
        self.decoded = self.operate_cipher()

    def get_decoded(self):
        """get the decoded text"""
        return self.decoded

    def operate_cipher(self):
        if(self.cipher and self.key):
            return self.cipher.decode(self.text, self.key)
        return "legg til cipher og key, og prøv igjen"
