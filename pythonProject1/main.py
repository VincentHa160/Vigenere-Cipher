# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class VigenereCipher:
    def __init__(self,keyword,word):
        self.word=word
        if not isinstance(keyword,str):
            raise TypeError("Keyword must be a string")
        if not keyword.isalpha():
            raise ValueError("Keyword must be uppercase")
        self.keyword=keyword
    #def combine_character(self,plain_letter,keyword_letter):
        #self.plain_letter=plain_letter
    def extend_keyword(self, length):
        self.realKeyword=""
        for i in range(length):
            while i>=len(self.keyword):
                i-=len(self.keyword)
            self.realKeyword+=self.keyword[i]
    def cipher(self):
        self.extend_keyword(len(self.word))
        self.ciphered=""
        for i in range(len(self.word)):
            self.ciphered+=chr(ord(self.realKeyword[i])+(ord(self.word[i])-ord('A')))
        return self.ciphered
    def reverse(self,ciphered):
        self.extend_keyword(len(ciphered))
        reversed=""
        for i in range(len(ciphered)):
            reversed += chr(ord(ciphered[i])-(ord(self.realKeyword[i])-ord('A')))
        return reversed


cipher=VigenereCipher("TRAIN","ENCODEINPYTHON")
print(cipher.cipher())
print(cipher.reverse(cipher.cipher()))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
