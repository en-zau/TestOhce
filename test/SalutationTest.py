class SalutationTest(unittest.TestCase):

    @parameterized.expand(
        [
            [LangueAnglaise(), "Hello"],
            [LangueFr(), "Bonjour"],
        ])
    def test_bonjour(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[0:len(attendu)])

    @parameterized.expand(
        [
            [LangueAnglaise(), "Goodbye"],
            [LangueFr(), "Au revoir"],
        ])
    def test_au_revoir(self, languechoisie, attendu):
        ohce = OhceBuilder().langue(languechoisie).build()
        resultat = ohce.palindrome("test")

        self.assertEqual(attendu, resultat[-len(attendu):])