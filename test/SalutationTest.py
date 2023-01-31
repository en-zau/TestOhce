import unittest

from parameterized import parameterized

from OhceBuilder import OhceBuilder
from src.langue.LangueAnglaise import LangueAnglaise
from src.langue.LangueFrancaise import LangueFrancaise
class SalutationTest(unittest.TestCase):

    @parameterized.expand(
        [
            [LangueAnglaise(), "Hello"],
            [LangueFrancaise(), "Bonjour"],
        ])
    def test_bonjour(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), "Goodbye"],
            [LangueFrancaise(), "Au revoir"],
        ])
    def test_au_revoir(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])