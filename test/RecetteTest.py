import datetime
import locale
import unittest

from OhceBuilder import OhceBuilder
from parameterized import parameterized

from src.Periodes import Periodes
from src.langue.Constantes import Constantes
from src.langue.LangueAnglaise import LangueAnglaise
from src.langue.LangueFrancaise import LangueFrancaise
from LangueSpy import LangueSpy


class PalindromeTest(unittest.TestCase):

    @parameterized.expand([
        [LangueAnglaise(), Constantes.Anglais.WELL_DONE, Constantes.Anglais.GOOD_BYE, Periodes.SOIR]
    ])
    #Automatique, palindrome, anglais, soir.
    def test_palindrome(self, languechoisie, bien_dit, au_revoir, periode):
        palindrome = "radar"

        ohce = OhceBuilder().langue(languechoisie).periode(periode).build()

        resultat = ohce.palindrome(palindrome)

        self.assertIn(palindrome + bien_dit + au_revoir, resultat)


    #Automatique, non-palindrome, français, matin.
    def test_non_palindrome(self):
        test = "palindrome"

        spy_langue = LangueSpy()
        ohce = OhceBuilder() \
            .langue(spy_langue) \
            .build()

        ohce.palindrome(test)

        self.assertEqual(0, spy_langue.nb_bien_dit)

    #Saisie libre du client, langue et moment actuels du système
    def test_client(self):
        locale_language, locale_encoding = locale.getlocale()
        current_time = datetime.datetime.now().time()
        chaine = input('Veuillez entrer une chaine à tester : ')

        if locale_language == 'fr_FR':
            langue_user = LangueFrancaise()
            if datetime.time(6) <= current_time < datetime.time(18):
                periode_user = Periodes.MATIN
                bonjour_user = Constantes.Francais.BONJOUR
            else:
                periode_user = Periodes.NUIT
                bonjour_user = Constantes.Francais.BONSOIR
            au_revoir_user = Constantes.Francais.AU_REVOIR
            bien_dit_user = Constantes.Francais.BIEN_DIT
        else:
            langue_user = LangueAnglaise()
            if datetime.time(6) <= current_time < datetime.time(12):
                periode_user = Periodes.MATIN
                bonjour_user = Constantes.Anglais.GOOD_MORNING
            elif datetime.time(12) <= current_time < datetime.time(18):
                periode_user = Periodes.APRES_MIDI
                bonjour_user = Constantes.Anglais.GOOD_AFTERNOON
            elif datetime.time(18) <= current_time < datetime.time(22):
                periode_user = Periodes.SOIR
                bonjour_user = Constantes.Anglais.GOOD_EVENING
            else:
                periode_user = Periodes.NUIT
                bonjour_user = Constantes.Anglais.GOOD_NIGHT
            au_revoir_user = Constantes.Anglais.GOOD_BYE
            bien_dit_user = Constantes.Anglais.WELL_DONE

        ohcebuild = OhceBuilder().langue(langue_user).periode(periode_user).build()

        result = ohcebuild.palindrome(chaine)

        self.assertIn(bonjour_user, result, au_revoir_user)


if __name__ == '__main__':
    unittest.main()