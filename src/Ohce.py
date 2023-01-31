class Ohce:

    def __init__(self, langue):
        self.__langue = langue

    def revert(self, chaine):
        return chaine[::-1]

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return self.bonjour() \
               + miroir \
               + (self.bien_dit() if miroir == palindrome else "") \
               + self.au_revoir()

    def bonjour(self):
        return self.__langue.bonjour()

    def bien_dit(self):
        return self.__langue.bien_dit()

    def au_revoir(self):
        return self.__langue.au_revoir()