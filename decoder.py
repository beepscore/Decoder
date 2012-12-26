#!/usr/local/bin/python3

# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Decoder:
    # In a class method, always list self as first parameter
    def __init__(self):

        self._cipher = {' ': ' ',
                      'a': 'A',
                      'b': 'B',
                      'c': 'C',
                      'd': 'D',
                      'e': 'E',
                      'f': 'F',
                      'g': 'G',
                      'h': 'H',
                      'i': 'I',
                      'j': 'J',
                      'k': 'K',
                      'l': 'L',
                      'm': 'M',
                      'n': 'N',
                      'o': 'O',
                      'p': 'P',
                      'q': 'Q',
                      'r': 'R',
                      's': 'S',
                      't': 'T',
                      'u': 'U',
                      'v': 'V',
                      'w': 'W',
                      'x': 'X',
                      'y': 'Y',
                      'z': 'Z' }

    #accessor method
    def get_cipher(self):
        return self._cipher

    def decode(self, aString):
        decodedString = ''
        for aChar in aString:
           decodedString = decodedString + self.get_cipher()[aChar]
        return decodedString

    
def main():

    decoder = Decoder(); 

    codedString = 'lsaj sdlfa'
    decodedString = decoder.decode(codedString)

    print(codedString)
    print(decodedString)

if __name__ == "__main__": main()

