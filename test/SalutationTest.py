import unittest

from src.Ohce import Ohce


class SalutationTest(unittest.TestCase):

    def test_bonjour(self):
        chaine = "Bonjour"

        ohce = Ohce()
        resultat = ohce.palindrome("test")

        self.assertEqual(chaine, resultat[0:len(chaine)])

    def test_au_revoir(self):
        chaine = "Au revoir"

        ohce = Ohce()
        resultat = ohce.palindrome("test")

        self.assertEqual(chaine, resultat[-len(chaine):])