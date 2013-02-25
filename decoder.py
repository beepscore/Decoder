#!/usr/bin/env python3

class Decoder:
    # In a class method, always list self as first parameter
    def __init__(self):
        print()

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

    # use dict() constructor method to avoid surrounding keys with ''
    cipher1 = dict(
              a = '_',
              b = 's',
              c = 'w',
              d = '_',
              e = '_',
              f = 'r',
              g = '_',
              h = '_',
              i = 'n',
              j = 't',
              k = '_',
              l = '_',
              m = 'h',
              n = '_',
              o = '_',
              p = '_',
              q = 'e',
              r = 'u',
              s = 'o',
              t = '_',
              u = '_',
              v = '_',
              w = 'f',
              x = '_',
              y = '_',
              z = 'm' )
    cipher1[' '] = ' '

    cipher2 = dict(
              a = 'm',
              b = 'f',
              c = '_',
              d = 'u',
              e = 'd',
              f = 'h',
              g = '_',
              h = '_',
              i = '_',
              j = 'r',
              k = '_',
              l = '_',
              m = 'i',
              n = 'b',
              o = 'l',
              p = 'g',
              q = 'o',
              r = 'n',
              s = '_',
              t = 's',
              u = '_',
              v = 'a',
              w = '_',
              x = 'e',
              y = '_',
              z = 't' )
    cipher2[' '] = ' '

    cipher12 = {' ': ' ',
              'a': '_',
              'b': 's',
              'c': '_',
              'd': '_',
              'e': '_',
              'f': '_',
              'g': '_',
              'h': '_',
              'i': '_',
              'j': 'a',
              'k': '_',
              'l': '_',
              'm': 'r',
              'n': '_',
              'o': '_',
              'p': 'n',
              'q': 'e',
              'r': '_',
              's': '_',
              't': '_',
              'u': '_',
              'v': '_',
              'w': '_',
              'x': '_',
              'y': '_',
              'z': 'm' }

    cipher13 = {' ': ' ',
              'a': '_',
              'b': 's',
              'c': '_',
              'd': '_',
              'e': '_',
              'f': 'e',
              'g': '_',
              'h': '_',
              'i': '_',
              'j': 'a',
              'k': '_',
              'l': '_',
              'm': 'r',
              'n': 't',
              'o': '_',
              'p': 't',
              'q': 'o',
              'r': '_',
              's': 'r',
              't': 'd',
              'u': 'a',
              'v': '_',
              'w': '_',
              'x': '_',
              'y': '_',
              'z': 'h' }

    cipher14 = {' ': ' ',
              'a': '_',
              'b': 'l',
              'c': '_',
              'd': '_',
              'e': '_',
              'f': 'e',
              'g': '_',
              'h': '_',
              'i': '_',
              'j': 't',
              'k': '_',
              'l': '_',
              'm': 'r',
              'n': 't',
              'o': '_',
              'p': 'o',
              'q': 'o',
              'r': '_',
              's': 'r',
              't': 'd',
              'u': 'a',
              'v': '_',
              'w': 'o',
              'x': '_',
              'y': '_',
              'z': 'k' }

    decodedString = decoder.decode(clue1, cipher1)
    print(decoder.spacedString(clue1))
    print(decoder.spacedString(decodedString))

    decodedString = decoder.decode(clue1, cipher12)
    print(decoder.spacedString(decodedString))

    decodedString = decoder.decode(clue1, cipher13)
    print(decoder.spacedString(decodedString))

    decodedString = decoder.decode(clue1, cipher14)
    print(decoder.spacedString(decodedString))
    print()

    # decodedString = decoder.decode(clue2, cipher2)
    # print(decoder.spacedString(clue2))
    # print(decoder.spacedString(decodedString))
    # print()

if __name__ == "__main__": main()

