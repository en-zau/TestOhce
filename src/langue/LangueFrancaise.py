from src.Periodes import Periodes
from src.langue.Constantes import Constantes


class LangueFrancaise:

    def bonjour(self, periode):
        if periode in (Periodes.SOIR, Periodes.NUIT):
            return Constantes.Francais.BONSOIR
        return Constantes.Francais.BONJOUR


    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT


    def au_revoir(self):
        return Constantes.Francais.AU_REVOIR
