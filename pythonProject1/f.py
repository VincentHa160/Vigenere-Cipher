class VigenereCipher:
    def __init__(self,keyword):
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
    def get_word(self,word):
        self.word=word
        self.extend_keyword(len(self.word))
    def cipher(self):
        self.ciphered=""
        for i in range(len(self.word)):
            self.ciphered+=chr(ord(self.realKeyword[i])+(ord(self.word[i])-ord(self.realKeyword[i])))
        return self.ciphered

cipher=VigenereCipher("a")
cipher.get_word("b")
print(cipher.cipher())
