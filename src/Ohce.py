class Ohce:
    def revert(self, chaine):
        return chaine[::-1]

    def palindrome(self, palindrome):
        miroir = palindrome[::-1]
        return "Bonjour" \
               + miroir \
               + ("Bien dit" if miroir == palindrome else "") \
               + "Au revoir"