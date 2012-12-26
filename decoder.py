#!/usr/local/bin/python3

# syntax.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Decoder:
    # In a class method, always list self as first parameter
    def __init__(self):
        print("init")

    def decode(self, aString, aCipher):

        aString = aString.lower()

        decodedString = ''
        for aChar in aString:
           decodedString = decodedString + aCipher[aChar]
        return decodedString

    # inserts spaces in string to visually separate underscore characters
    def spacedString(self, aString):
        spacedString = ''
        for aChar in aString:
           spacedString = spacedString + aChar + ' '
        return spacedString
    
def main():

    decoder = Decoder(); 

    clue1 = "Jp wqfht ups csij bqqz jmq zrstfqn xkohtf tpnjmlknai"
    clue2 = "Zfxjx vjx v rdanxj qb nvoo nxvjmrpt mrtmex zfx Mtmt"
    clue3 = "Grb yfqq ytfzdmxj wfm fqrfsj yt ctfze dmjdet, ykg sbk mtte gb ctfz gcztt yfqq ytfzdmxj du sbk rfmg gb hzbxztjj"

    cipher1 = {' ': ' ',
              'a': '_',
              'b': '_',
              'c': '_',
              'd': '_',
              'e': '_',
              'f': '_',
              'g': '_',
              'h': '_',
              'i': '_',
              'j': '_',
              'k': '_',
              'l': '_',
              'm': '_',
              'n': '_',
              'o': '_',
              'p': '_',
              'q': '_',
              'r': '_',
              's': '_',
              't': '_',
              'u': '_',
              'v': '_',
              'w': '_',
              'x': '_',
              'y': '_',
              'z': '_' }

    cipher2 = {' ': ' ',
              'a': '_',
              'b': '_',
              'c': '_',
              'd': '_',
              'e': '_',
              'f': '_',
              'g': '_',
              'h': '_',
              'i': '_',
              'j': '_',
              'k': '_',
              'l': '_',
              'm': '_',
              'n': '_',
              'o': '_',
              'p': '_',
              'q': '_',
              'r': '_',
              's': '_',
              't': '_',
              'u': '_',
              'v': '_',
              'w': '_',
              'x': '_',
              'y': '_',
              'z': '_' }

    decodedString = decoder.decode(clue2, cipher2)

    print(decoder.spacedString(clue2))
    print(decoder.spacedString(decodedString))

if __name__ == "__main__": main()

