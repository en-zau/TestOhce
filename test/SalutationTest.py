import unittest

from parameterized import parameterized

from OhceBuilder import OhceBuilder
from OhceBuilder import OhceBuilder
from src.langue.LangueAnglaise import LangueAnglaise
from src.langue.LangueFrancaise import LangueFrancaise

    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.HELLO],
            [LangueFrancaise(), Constantes.Francais.BONJOUR],
        ])
    def test_bonjour(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
	@@ -22,8 +23,8 @@ def test_bonjour(self, languechoisie, attendu):

    @parameterized.expand(
        [
            [LangueAnglaise(), Constantes.Anglais.GOOD_BYE],
            [LangueFrancaise(), Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])