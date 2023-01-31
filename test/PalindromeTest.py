import unittest
from parameterized import parameterized
from src.langue.LangueAnglaise import LangueAnglaise
from src.langue.LangueFrancaise import LangueFrancaise

from OhceBuilder import OhceBuilder

class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        ohce = OhceBuilder.default()
        chaine_renvoye = ohce.revert(chaine)

        self.assertIn(chaine[::-1], chaine_renvoye)

    @parameterized.expand([
        [LangueAnglaise(), "Well done"],
        [LangueFrancaise(), "Bien dit"],
    ])
    def test_palindrome(self, languechoisie, bien_dit):
        palindrome = "radar"

        ohce = OhceBuilder().langue(languechoisie).build()

        resultat = ohce.palindrome(palindrome)
        self.assertIn(palindrome, resultat)

        resultat_apres_palindrome = resultat[len(palindrome):len(resultat)]
        self.assertIn(palindrome + bien_dit, resultat_apres_palindrome)


if __name__ == '__main__':
    unittest.main()