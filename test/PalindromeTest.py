import unittest
from src.Ohce import Ohce

class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "oula"


        ohce = Ohce()
        chaine_renvoye = ohce.revert(chaine)

        self.assertIn(chaine[::-1], chaine_renvoye)

    def test_palindrome(self):
        chaine = "radar"
        ohce = Ohce()
        chaine_renvoye = ohce.revert(chaine)
        self.assertIn(chaine_renvoye, chaine)

        resultat_apres_palindrome = ohce.palindrome(chaine)
        self.assertIn(chaine + "Bien dit", resultat_apres_palindrome)


if __name__ == '__main__':
    unittest.main()