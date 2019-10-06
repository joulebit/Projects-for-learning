# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 06:55:29 2019

@author: Joule
"""

from sender_reciever import Reciever, Sender
from affine import Affine
from ubrytelig import Ubrytelig

class Hacker(Reciever):
    """Brute force hacker!
    Denne versjonen trenger ikke å få det brukte cipheret som input,
    hvis cipheret er det Ubrytelige,
    tar dekrypteringen bare 52 sekunder lengre"""

    def __init__(self):
        Reciever.__init__(self)
        _f = open('english_words.txt', "r")
        self.valid_words = set(_f.read().split())
        self.valid_inverse = [1, 2, 3, 4, 6, 7, 8, 9, 11,\
                              12, 13, 14, 16, 17, 18, 21,
                              22, 23, 24, 26, 27, 28, 29,
                              31, 32, 33, 34, 36, 37, 39,
                              41, 42, 43, 44, 46, 47, 48,
                              49, 51, 52, 53, 54, 56, 58,
                              59, 61, 62, 63, 64, 66, 67,
                              68, 69, 71, 72, 73, 74, 77,
                              78, 79, 81, 82, 83, 84, 86,
                              87, 88, 89, 91, 92, 93, 94]
        _f.close()

    def decode(self, text):
        guessed_word = ''
        words_recognized_record = 0
        dummy = Reciever()
        dummy.set_cipher(Affine())
        """Tester for Affine cipher, siden det også plukker opp alle
        multiplikasjon og alle Caesar"""
        for multiply in self.valid_inverse:
            for add in range(95):
                dummy.set_key((multiply, add))
                dummy.decode(text)
                decoded_text = dummy.get_decoded().lower().split()
                matching_words = set(decoded_text).intersection(self.valid_words)
                if len(matching_words) > words_recognized_record:
                    words_recognized_record = len(matching_words)
                    guessed_word = " ".join(decoded_text)

            """Hvis vi kjenner igjen minst tre ord, så kan vi stoppe
            searchet tidlig og spare opp til ca 50 sekunder"""
            if words_recognized_record >= 3:
                return guessed_word

        """Ellers må vi annta at det "ubrytelige" cipheret ble brukt"""
        """10 min å hacke med kodeord "pizza"...
        og 30 sekund å hacke med kodeord "ant"... """
        dummy.set_cipher(Ubrytelig())
        count = 1
        for kodeord in self.valid_words:
            dummy.set_key(kodeord)
            dummy.decode(text)
            decoded_text = dummy.get_decoded().lower().split()
            #For å visualisere hvor langt dekrypteringen har kommet i fase 2
            print(decoded_text, count)
            count += 1
            #Denne operasjonen koster sykt mye
            matching_words = set(decoded_text).intersection(self.valid_words)
            if len(matching_words) > words_recognized_record:
                words_recognized_record = len(matching_words)
                guessed_word = " ".join(decoded_text)

            if words_recognized_record >= 5:
                print("Kodeordet er", kodeord)
                return guessed_word

        else:
            return "Could not brute force the message"




A = Sender()
#A.set_key((2,0))
#A.set_cipher(Affine())
A.set_key("pizza")
A.set_cipher(Ubrytelig())
A.encode("To recieve full marks you have to solve all parts")
#Print how the encrypted text looks like
print(A.get_encoded())
H = Hacker()
print(H.decode(A.get_encoded()))
