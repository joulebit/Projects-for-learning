# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 13:33:10 2019

@author: Joule
"""

class Person:
    """supersclass for sender, reciever and hacker"""

    def __init__(self):
        self.key = ''
        self.cipher = None

    def set_key(self, key):
        """Set the key for the given person to use"""
        self.key = key

    def get_key(self):
        """get the given key this object has"""
        return self.key

    def set_cipher(self, cipher):
        """Set the type of Cipher is being used"""
        self.cipher = cipher

    def get_cipher(self):
        """get the type of cipher which is being used"""
        return self.cipher

    def operate_cipher(self):
        """method each individual subclass will implement"""
        pass
