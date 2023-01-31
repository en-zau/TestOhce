import unittest


class SalutationTest(unittest.TestCase):

    def test_bonjour(self):
        chaine = "Bonjour"

        resultat = palindrome("test")

        self.assertEqual(chaine, resultat[0:len(chaine)])

    def test_au_revoir(self):
        chaine = "Au revoir"

        resultat = palindrome("test")

        self.assertEqual(chaine, resultat[-len(chaine):])