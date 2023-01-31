import unittest


class PalindromeTest(unittest.TestCase):
    def test_renvoi_miroir(self):
        chaine = "toto"

        chaine_renvoye = revert(chaine)

        self.assertIn(chaine[::-1], chaine_renvoye)

    def test_palindrome(self):
        chaine = "radar"
        chaine_renvoye = revert(chaine)
        self.assertIn(chaine_renvoye, chaine)

        resultat_apres_palindrome = palindrome(chaine)
        self.assertIn(chaine + "Bien dit", resultat_apres_palindrome)


if __name__ == '__main__':
    unittest.main()