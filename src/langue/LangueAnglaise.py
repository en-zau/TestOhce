from src.Periodes import Periodes
from src.langue.Constantes import Constantes
class LangueAnglaise:

    def bonjour(self, periode ):
        match periode:
            case Periodes.MATIN:
                return Constantes.Anglais.GOOD_MORNING
            case Periodes.APRES_MIDI:
                return Constantes.Anglais.GOOD_AFTERNOON
            case Periodes.SOIR:
                return Constantes.Anglais.GOOD_EVENING
            case Periodes.NUIT:
                return Constantes.Anglais.GOOD_NIGHT
        return Constantes.Anglais.HELLO

    def bien_dit(self):
        return Constantes.Anglais.WELL_DONE

    def au_revoir(self):
        return Constantes.Anglais.GOOD_BYE
